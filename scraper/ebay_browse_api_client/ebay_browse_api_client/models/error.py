from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.error_parameter import ErrorParameter
from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """The type that defines the fields that can be returned in an error.

    Attributes:
        category (Union[Unset, str]): This string value indicates the error category. There are three categories of
            errors: request errors, application errors, and system errors.
        domain (Union[Unset, str]): The name of the primary system where the error occurred. This is relevant for
            application errors.
        error_id (Union[Unset, int]): A unique code that identifies the particular error or warning that occurred. Your
            application can use error codes as identifiers in your customized error-handling algorithms.
        input_ref_ids (Union[Unset, List[str]]): An array of reference IDs that identify the specific request elements
            most closely associated to the error or warning, if any.
        long_message (Union[Unset, str]): A detailed description of the condition that caused the error or warning, and
            information on what to do to correct the problem.
        message (Union[Unset, str]): A description of the condition that caused the error or warning.
        output_ref_ids (Union[Unset, List[str]]): An array of reference IDs that identify the specific response elements
            most closely associated to the error or warning, if any.
        parameters (Union[Unset, List[ErrorParameter]]): An array of warning and error messages that return one or more
            variables contextual information about the error or warning. This is often the field or value that triggered the
            error or warning.
        subdomain (Union[Unset, str]): The name of the subdomain in which the error or warning occurred.
    """

    category: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    error_id: Union[Unset, int] = UNSET
    input_ref_ids: Union[Unset, List[str]] = UNSET
    long_message: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    output_ref_ids: Union[Unset, List[str]] = UNSET
    parameters: Union[Unset, List[ErrorParameter]] = UNSET
    subdomain: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        domain = self.domain
        error_id = self.error_id
        input_ref_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.input_ref_ids, Unset):
            input_ref_ids = self.input_ref_ids

        long_message = self.long_message
        message = self.message
        output_ref_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.output_ref_ids, Unset):
            output_ref_ids = self.output_ref_ids

        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()

                parameters.append(parameters_item)

        subdomain = self.subdomain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if domain is not UNSET:
            field_dict["domain"] = domain
        if error_id is not UNSET:
            field_dict["errorId"] = error_id
        if input_ref_ids is not UNSET:
            field_dict["inputRefIds"] = input_ref_ids
        if long_message is not UNSET:
            field_dict["longMessage"] = long_message
        if message is not UNSET:
            field_dict["message"] = message
        if output_ref_ids is not UNSET:
            field_dict["outputRefIds"] = output_ref_ids
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category", UNSET)

        domain = d.pop("domain", UNSET)

        error_id = d.pop("errorId", UNSET)

        input_ref_ids = cast(List[str], d.pop("inputRefIds", UNSET))

        long_message = d.pop("longMessage", UNSET)

        message = d.pop("message", UNSET)

        output_ref_ids = cast(List[str], d.pop("outputRefIds", UNSET))

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = ErrorParameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        subdomain = d.pop("subdomain", UNSET)

        error = cls(
            category=category,
            domain=domain,
            error_id=error_id,
            input_ref_ids=input_ref_ids,
            long_message=long_message,
            message=message,
            output_ref_ids=output_ref_ids,
            parameters=parameters,
            subdomain=subdomain,
        )

        error.additional_properties = d
        return error

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
