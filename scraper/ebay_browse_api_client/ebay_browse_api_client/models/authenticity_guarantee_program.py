from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticityGuaranteeProgram")


@attr.s(auto_attribs=True)
class AuthenticityGuaranteeProgram:
    """A type that identifies whether the item is qualified for the Authenticity Guarantee program.

    Attributes:
        description (Union[Unset, str]): An indication that the item is qualified for the Authenticity Guarantee
            program.
        terms_web_url (Union[Unset, str]): The URL to the Authenticity Guarantee program terms of use.
    """

    description: Union[Unset, str] = UNSET
    terms_web_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        terms_web_url = self.terms_web_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if terms_web_url is not UNSET:
            field_dict["termsWebUrl"] = terms_web_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        terms_web_url = d.pop("termsWebUrl", UNSET)

        authenticity_guarantee_program = cls(
            description=description,
            terms_web_url=terms_web_url,
        )

        authenticity_guarantee_program.additional_properties = d
        return authenticity_guarantee_program

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
