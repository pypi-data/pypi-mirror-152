from typing import Any, Optional, Tuple, Dict
from falcon import Request
from ioclib.injector import Requirement, void


def header(default=void) -> Any:
    return Requirement[Any](None, None, 'falcon/header', default)


def parameter(default=void) -> Any:
    return Requirement[Any](None, None, 'falcon/parameter', default)


def context(default=void) -> Any:
    return Requirement[Any](None, None, 'falcon/context', default)


def falcon_request_injector(requirement: Requirement[Any], args: Tuple[Any, ...], kwargs: Dict[str, Any]):
    if not requirement.location.startswith('falcon'):
        raise LookupError()

    request = _get_request(args)

    if not request:
        raise ValueError()

    if requirement.location == 'falcon/parameter':
        if issubclass(requirement.type, str):
            return request.get_param(requirement.name, False)

        if issubclass(requirement.type, int):
            return request.get_param_as_int(requirement.name, False)

        if issubclass(requirement.type, float):
            return request.get_param_as_float(requirement.name, False)

        if issubclass(requirement.type, list):
            return request.get_param_as_list(requirement.name, False)

        if issubclass(requirement.type, dict):
            return request.get_param_as_json(requirement.name, False)

        raise ValueError()

    if requirement.location == 'falcon/context':
        return getattr(request.context, requirement.name)

    if requirement.location == 'falcon/header':
        raise NotImplementedError()


def _get_request(args: Tuple[Any, ...]) -> Optional[Request]:
    for arg in args:
        if isinstance(arg, Request):
            return arg
