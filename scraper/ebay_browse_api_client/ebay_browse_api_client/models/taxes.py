from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.tax_jurisdiction import TaxJurisdiction
from ..types import UNSET, Unset

T = TypeVar("T", bound="Taxes")


@attr.s(auto_attribs=True)
class Taxes:
    """The type that defines the tax fields.

    Attributes:
        ebay_collect_and_remit_tax (Union[Unset, bool]): This field is only returned if <code>true</code>, and indicates
            that eBay will collect tax (sales tax, Goods and Services tax, or VAT) for at least one line item in the order,
            and remit the tax to the taxing authority of the buyer's residence.
        included_in_price (Union[Unset, bool]): This indicates if tax was applied for the cost of the item.
        shipping_and_handling_taxed (Union[Unset, bool]): This indicates if tax is applied for the shipping cost.
        tax_jurisdiction (Union[Unset, TaxJurisdiction]): The type that defines the fields for the tax jurisdiction
            details.
        tax_percentage (Union[Unset, str]): The percentage of tax.
        tax_type (Union[Unset, str]): This field indicates the type of tax that may be collected for the item. For
            implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:TaxType'>eBay
            API documentation</a>
    """

    ebay_collect_and_remit_tax: Union[Unset, bool] = UNSET
    included_in_price: Union[Unset, bool] = UNSET
    shipping_and_handling_taxed: Union[Unset, bool] = UNSET
    tax_jurisdiction: Union[Unset, TaxJurisdiction] = UNSET
    tax_percentage: Union[Unset, str] = UNSET
    tax_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ebay_collect_and_remit_tax = self.ebay_collect_and_remit_tax
        included_in_price = self.included_in_price
        shipping_and_handling_taxed = self.shipping_and_handling_taxed
        tax_jurisdiction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax_jurisdiction, Unset):
            tax_jurisdiction = self.tax_jurisdiction.to_dict()

        tax_percentage = self.tax_percentage
        tax_type = self.tax_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ebay_collect_and_remit_tax is not UNSET:
            field_dict["ebayCollectAndRemitTax"] = ebay_collect_and_remit_tax
        if included_in_price is not UNSET:
            field_dict["includedInPrice"] = included_in_price
        if shipping_and_handling_taxed is not UNSET:
            field_dict["shippingAndHandlingTaxed"] = shipping_and_handling_taxed
        if tax_jurisdiction is not UNSET:
            field_dict["taxJurisdiction"] = tax_jurisdiction
        if tax_percentage is not UNSET:
            field_dict["taxPercentage"] = tax_percentage
        if tax_type is not UNSET:
            field_dict["taxType"] = tax_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ebay_collect_and_remit_tax = d.pop("ebayCollectAndRemitTax", UNSET)

        included_in_price = d.pop("includedInPrice", UNSET)

        shipping_and_handling_taxed = d.pop("shippingAndHandlingTaxed", UNSET)

        _tax_jurisdiction = d.pop("taxJurisdiction", UNSET)
        tax_jurisdiction: Union[Unset, TaxJurisdiction]
        if isinstance(_tax_jurisdiction, Unset):
            tax_jurisdiction = UNSET
        else:
            tax_jurisdiction = TaxJurisdiction.from_dict(_tax_jurisdiction)

        tax_percentage = d.pop("taxPercentage", UNSET)

        tax_type = d.pop("taxType", UNSET)

        taxes = cls(
            ebay_collect_and_remit_tax=ebay_collect_and_remit_tax,
            included_in_price=included_in_price,
            shipping_and_handling_taxed=shipping_and_handling_taxed,
            tax_jurisdiction=tax_jurisdiction,
            tax_percentage=tax_percentage,
            tax_type=tax_type,
        )

        taxes.additional_properties = d
        return taxes

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
