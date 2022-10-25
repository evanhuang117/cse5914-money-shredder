from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    """The type that defines the fields for an address.

    Attributes:
        address_line_1 (Union[Unset, str]): The first line of the street address. <b> Note: </b> This is conditionally
            returned in the <b> itemLocation</b> field.
        address_line_2 (Union[Unset, str]): The second line of the street address. This field is not always used, but
            can be used for 'Suite Number' or 'Apt Number'.
        city (Union[Unset, str]): The city of the address.
        country (Union[Unset, str]): The two-letter <a href="https://www.iso.org/iso-3166-country-codes.html "
            target="_blank">ISO 3166</a> standard of the country of the address. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/ba:CountryCodeEnum'>eBay API documentation</a>
        county (Union[Unset, str]): The county of the address.
        postal_code (Union[Unset, str]): The postal code (or zip code in US) code of the address. Sellers set a postal
            code (or zip code in US) for items when they are listed. The postal code is used for calculating proximity
            searches. It is anonymized when returned in <b>itemLocation.postalCode</b> via the API.
        state_or_province (Union[Unset, str]): The state or province of the address.  <b> Note: </b> This is
            conditionally returned in the <b> itemLocation</b> field.
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    county: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    state_or_province: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_line_1 = self.address_line_1
        address_line_2 = self.address_line_2
        city = self.city
        country = self.country
        county = self.county
        postal_code = self.postal_code
        state_or_province = self.state_or_province

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if county is not UNSET:
            field_dict["county"] = county
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if state_or_province is not UNSET:
            field_dict["stateOrProvince"] = state_or_province

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        county = d.pop("county", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        state_or_province = d.pop("stateOrProvince", UNSET)

        address = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            country=country,
            county=county,
            postal_code=postal_code,
            state_or_province=state_or_province,
        )

        address.additional_properties = d
        return address

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
