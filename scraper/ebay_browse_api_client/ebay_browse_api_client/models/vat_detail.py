from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VatDetail")


@attr.s(auto_attribs=True)
class VatDetail:
    """The type the defines the fields for the VAT (value add tax) information.

    Attributes:
        issuing_country (Union[Unset, str]): The two-letter <a href="https://www.iso.org/iso-3166-country-codes.html "
            target="_blank">ISO 3166</a> standard of the country issuing the seller's VAT (value added tax) ID. VAT is a tax
            added by some European countries. For implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/ba:CountryCodeEnum'>eBay API documentation</a>
        vat_id (Union[Unset, str]): The seller's VAT (value added tax) ID. VAT is a tax added by some European
            countries.
    """

    issuing_country: Union[Unset, str] = UNSET
    vat_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuing_country = self.issuing_country
        vat_id = self.vat_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuing_country is not UNSET:
            field_dict["issuingCountry"] = issuing_country
        if vat_id is not UNSET:
            field_dict["vatId"] = vat_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issuing_country = d.pop("issuingCountry", UNSET)

        vat_id = d.pop("vatId", UNSET)

        vat_detail = cls(
            issuing_country=issuing_country,
            vat_id=vat_id,
        )

        vat_detail.additional_properties = d
        return vat_detail

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
