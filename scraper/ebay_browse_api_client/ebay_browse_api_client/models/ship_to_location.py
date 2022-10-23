from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipToLocation")


@attr.s(auto_attribs=True)
class ShipToLocation:
    """The type that defines the fields for the country and postal code of where an item is to be shipped.

    Attributes:
        country (Union[Unset, str]): The two-letter <a href="https://www.iso.org/iso-3166-country-codes.html "
            target="_blank">ISO 3166</a> standard of the country for where the item is to be shipped. For implementation
            help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/ba:CountryCodeEnum'>eBay API
            documentation</a>
        postal_code (Union[Unset, str]): The zip code (postal code) for where the item is to be shipped.
    """

    country: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country = self.country
        postal_code = self.postal_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country = d.pop("country", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        ship_to_location = cls(
            country=country,
            postal_code=postal_code,
        )

        ship_to_location.additional_properties = d
        return ship_to_location

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
