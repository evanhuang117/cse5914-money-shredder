from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error import Error
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompatibilityResponse")


@attr.s(auto_attribs=True)
class CompatibilityResponse:
    """The type that defines the response fields for <b> checkCompatibility</b>.

    Attributes:
        compatibility_status (Union[Unset, str]): An enumeration value that tells you if the item is compatible with the
            product. <br /><br />The values are: <ul>   <li>   <b> COMPATIBLE</b> - Indicates the item is compatible with
            the product specified in the request.</li>   <li>   <b> NOT_COMPATIBLE</b> - Indicates the item is not
            compatible with the product specified in the request. Be sure to check all the <b> value</b> fields to ensure
            they are correct as errors in the value can also cause this response.</li>   <li> <b> UNDETERMINED</b> -
            Indicates one or more attributes for the specified product are missing so compatibility cannot be determined.
            The response returns the attributes that are missing.</li>  </ul>  Code so that your app gracefully handles any
            future changes to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/gct:CompatibilityStatus'>eBay API documentation</a>
        warnings (Union[Unset, List[Error]]): An array of warning messages. These types of errors do not prevent the
            method from executing but should be checked.
    """

    compatibility_status: Union[Unset, str] = UNSET
    warnings: Union[Unset, List[Error]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compatibility_status = self.compatibility_status
        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()

                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compatibility_status is not UNSET:
            field_dict["compatibilityStatus"] = compatibility_status
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compatibility_status = d.pop("compatibilityStatus", UNSET)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        compatibility_response = cls(
            compatibility_status=compatibility_status,
            warnings=warnings,
        )

        compatibility_response.additional_properties = d
        return compatibility_response

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
