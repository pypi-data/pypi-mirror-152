import argparse
import collections.abc
import pprint
from typing import Union, List, Dict, Optional


from tmtccmd.logging import get_console_logger
from tmtccmd.utility.conf_util import check_args_in_dict
from spacepackets.ecss.conf import (
    PusVersion,
    set_default_tc_apid,
    set_default_tm_apid,
    set_pus_tc_version,
    set_pus_tm_version,
)
from tmtccmd.core.globals_manager import update_global, get_global
from .definitions import (
    CoreGlobalIds,
    CoreModeList,
    CoreServiceList,
    CoreModeStrings,
    CoreComInterfacesDict,
    CoreComInterfaces,
    DEBUG_MODE,
    ServiceOpCodeDictT,
    OpCodeDictKeys,
    ComIFDictT,
    OpCodeEntryT,
    OpCodeOptionsT,
    OpCodeNameT,
)
from tmtccmd.com_if.com_if_utilities import determine_com_if

LOGGER = get_console_logger()
SERVICE_OP_CODE_DICT = dict()


def set_json_cfg_path(json_cfg_path: str):
    update_global(CoreGlobalIds.JSON_CFG_PATH, json_cfg_path)


def get_json_cfg_path() -> str:
    return get_global(CoreGlobalIds.JSON_CFG_PATH)


def set_glob_com_if_dict(custom_com_if_dict: ComIFDictT):
    CoreComInterfacesDict.update(custom_com_if_dict)
    update_global(CoreGlobalIds.COM_IF_DICT, CoreComInterfacesDict)


def get_glob_com_if_dict() -> ComIFDictT:
    return get_global(CoreGlobalIds.COM_IF_DICT)


def set_default_globals_pre_args_parsing(
    gui: bool,
    tc_apid: int,
    tm_apid: int,
    pus_tc_version: PusVersion = PusVersion.PUS_C,
    pus_tm_version: PusVersion = PusVersion.PUS_C,
    com_if_id: str = CoreComInterfaces.DUMMY.value,
    custom_com_if_dict=None,
    display_mode="long",
    tm_timeout: float = 4.0,
    print_to_file: bool = True,
    tc_send_timeout_factor: float = 2.0,
):
    if custom_com_if_dict is None:
        custom_com_if_dict = dict()
    set_default_tc_apid(tc_apid=tc_apid)
    set_default_tm_apid(tm_apid=tm_apid)
    set_pus_tc_version(pus_tc_version)
    set_pus_tm_version(pus_tm_version)
    update_global(CoreGlobalIds.COM_IF, com_if_id)
    update_global(CoreGlobalIds.TC_SEND_TIMEOUT_FACTOR, tc_send_timeout_factor)
    update_global(CoreGlobalIds.TM_TIMEOUT, tm_timeout)
    update_global(CoreGlobalIds.DISPLAY_MODE, display_mode)
    update_global(CoreGlobalIds.PRINT_TO_FILE, print_to_file)
    update_global(CoreGlobalIds.CURRENT_SERVICE, CoreServiceList.SERVICE_17.value)
    update_global(CoreGlobalIds.SERIAL_CONFIG, dict())
    update_global(CoreGlobalIds.ETHERNET_CONFIG, dict())
    set_glob_com_if_dict(custom_com_if_dict=custom_com_if_dict)
    pp = pprint.PrettyPrinter()
    update_global(CoreGlobalIds.PRETTY_PRINTER, pp)
    update_global(CoreGlobalIds.TM_LISTENER_HANDLE, None)
    update_global(CoreGlobalIds.COM_INTERFACE_HANDLE, None)
    update_global(CoreGlobalIds.TMTC_PRINTER_HANDLE, None)
    update_global(CoreGlobalIds.PRINT_RAW_TM, False)
    update_global(CoreGlobalIds.USE_LISTENER_AFTER_OP, True)
    update_global(CoreGlobalIds.RESEND_TC, False)
    update_global(CoreGlobalIds.OP_CODE, "0")
    update_global(CoreGlobalIds.MODE, CoreModeList.LISTENER_MODE)


def handle_mode_arg(
    args,
    custom_modes_list: Union[None, List[Union[collections.abc.Iterable, dict]]] = None,
) -> int:
    # Determine communication interface from arguments. Must be contained in core modes list
    try:
        mode_param = args.mode
    except AttributeError:
        LOGGER.warning("Passed namespace does not contain the mode (-m) argument")
        mode_param = CoreModeList.LISTENER_MODE
    mode_param = check_and_set_core_mode_arg(
        mode_arg=mode_param, custom_modes_list=custom_modes_list
    )
    update_global(CoreGlobalIds.MODE, mode_param)
    return mode_param


def handle_com_if_arg(
    args, json_cfg_path: str, custom_com_if_dict: Dict[str, any] = None
):
    all_com_ifs = CoreComInterfacesDict
    if custom_com_if_dict is not None:
        all_com_ifs = CoreComInterfacesDict.update(custom_com_if_dict)
    try:
        com_if_key = str(args.com_if)
    except AttributeError:
        LOGGER.warning("No communication interface specified")
        LOGGER.warning("Trying to set from existing configuration..")
        com_if_key = determine_com_if(
            com_if_dict=all_com_ifs, json_cfg_path=json_cfg_path
        )
    if com_if_key == CoreComInterfaces.UNSPECIFIED.value:
        com_if_key = determine_com_if(
            com_if_dict=all_com_ifs, json_cfg_path=json_cfg_path
        )
    update_global(CoreGlobalIds.COM_IF, com_if_key)
    try:
        LOGGER.info(f"Communication interface: {all_com_ifs[com_if_key]}")
    except KeyError as e:
        LOGGER.error(f"Invalid communication interface key {com_if_key}, error {e}")


def check_and_set_other_args(args):
    if args.listener is not None:
        update_global(CoreGlobalIds.USE_LISTENER_AFTER_OP, args.listener)
    if args.tm_timeout is not None:
        update_global(CoreGlobalIds.TM_TIMEOUT, args.tm_timeout)
    if args.print_hk is not None:
        update_global(CoreGlobalIds.PRINT_HK, args.print_hk)
    if args.print_tm is not None:
        update_global(CoreGlobalIds.PRINT_TM, args.print_tm)
    if args.raw_print is not None:
        update_global(CoreGlobalIds.PRINT_RAW_TM, args.raw_print)
    if args.print_log is not None:
        update_global(CoreGlobalIds.PRINT_TO_FILE, args.print_log)
    if args.resend_tc is not None:
        update_global(CoreGlobalIds.RESEND_TC, args.resend_tc)
    update_global(CoreGlobalIds.TC_SEND_TIMEOUT_FACTOR, 3)


def check_and_set_core_mode_arg(
    mode_arg: any,
    custom_modes_list: Union[None, List[Union[dict, collections.abc.Iterable]]] = None,
) -> int:
    """Checks whether the mode argument is contained inside the core mode list integer enumeration
    or a custom mode list integer which can be passed optionally.
    This function will set the single command mode as the global mode parameter if the passed mode
    is not found in either enumerations.

    :param mode_arg:
    :param custom_modes_list:
    :return: Mode value which was set
    """
    in_enum, mode_value = check_args_in_dict(
        param=mode_arg, iterable=CoreModeList, warning_hint="mode integers"
    )
    if not in_enum:
        in_enum, mode_value = check_args_in_dict(
            param=mode_arg, iterable=CoreModeStrings, warning_hint="mode strings"
        )
    if in_enum:
        update_global(CoreGlobalIds.MODE, mode_value)
        return mode_value

    mode_arg_invalid = False
    if custom_modes_list is not None:
        for custom_mode_entry in custom_modes_list:
            in_enum, mode_value = check_args_in_dict(
                param=mode_arg, iterable=custom_mode_entry, warning_hint="custom mode"
            )
            if in_enum:
                break
        if not in_enum:
            mode_arg_invalid = True
    else:
        mode_arg_invalid = True

    if mode_arg_invalid:
        LOGGER.warning(
            f"Passed mode argument might be invalid, "
            f"setting to {CoreModeList.SEQUENTIAL_CMD_MODE}"
        )
        mode_value = CoreModeList.SEQUENTIAL_CMD_MODE
    update_global(CoreGlobalIds.MODE, mode_value)
    return mode_value


def check_and_set_core_service_arg(
    service_arg: any, custom_service_list: collections.abc.Iterable = None
):
    in_enum, service_value = check_args_in_dict(
        param=service_arg, iterable=CoreServiceList, warning_hint="service"
    )
    if in_enum:
        update_global(CoreGlobalIds.CURRENT_SERVICE, service_value)
        return

    service_arg_invalid = False
    if custom_service_list is not None:
        for custom_services_entry in custom_service_list:
            in_enum, service_value = check_args_in_dict(
                param=service_arg,
                iterable=custom_services_entry,
                warning_hint="custom mode",
            )
            if in_enum:
                break
        if not in_enum:
            service_arg_invalid = True
    else:
        service_arg_invalid = True

    if service_arg_invalid:
        LOGGER.warning(
            f"Passed service argument might be invalid, "
            f"setting to {CoreServiceList.SERVICE_17}"
        )
        service_value = CoreServiceList.SERVICE_17
    update_global(CoreGlobalIds.CURRENT_SERVICE, service_value)


def get_default_service_op_code_dict() -> ServiceOpCodeDictT:
    global SERVICE_OP_CODE_DICT
    service_op_code_dict = SERVICE_OP_CODE_DICT
    if service_op_code_dict == dict():
        op_code_dict_srv_5 = {
            "0": ("Event Test", {OpCodeDictKeys.TIMEOUT: 2.0}),
        }
        service_5_tuple = ("PUS Service 5 Event", op_code_dict_srv_5)
        op_code_dict_srv_17 = {
            "0": ("Ping Test", {OpCodeDictKeys.TIMEOUT: 2.2}),
        }
        service_17_tuple = ("PUS Service 17 Test", op_code_dict_srv_17)

        service_op_code_dict[CoreServiceList.SERVICE_5.value] = service_5_tuple
        service_op_code_dict[CoreServiceList.SERVICE_17.value] = service_17_tuple
        # SERVICE_OP_CODE_DICT = service_op_code_dict
    return service_op_code_dict


def add_op_code_entry(
    op_code_dict: OpCodeEntryT,
    keys: OpCodeNameT,
    info: str,
    options: OpCodeOptionsT = None,
):
    if isinstance(keys, str):
        keys = [keys]
    op_code_dict.update(OpCodeEntryT.fromkeys(keys, (info, options)))


def add_service_op_code_entry(
    srv_op_code_dict: ServiceOpCodeDictT,
    name: str,
    info: str,
    op_code_entry: OpCodeEntryT,
):
    srv_op_code_dict.update({name: (info, op_code_entry)})


def generate_op_code_options(
    enter_listener_mode: bool = False, custom_timeout: Optional[float] = None
) -> dict:
    op_code_opts = dict()
    op_code_opts.update({OpCodeDictKeys.ENTER_LISTENER_MODE: enter_listener_mode})
    if custom_timeout is not None:
        op_code_opts.update({OpCodeDictKeys.TIMEOUT: custom_timeout})
    return op_code_opts
