from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.converted_amount import ConvertedAmount
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShippingOptionSummary")


@attr.s(auto_attribs=True)
class ShippingOptionSummary:
    """The type that defines the fields for the shipping information.

    Attributes:
        guaranteed_delivery (Union[Unset, bool]): Indicates if the seller has committed to shipping the item with eBay
            Guaranteed Delivery. With eBay Guaranteed Delivery, the  seller is committed to getting the line item to the
            buyer within 4 business days or less. See the <a href="https://www.ebay.com/help/buying/shipping-
            delivery/buying-items-ebay-guaranteed-delivery?id=4641 ">Buying items with eBay Guaranteed Delivery</a> help
            topic for more details about eBay Guaranteed Delivery.
        max_estimated_delivery_date (Union[Unset, str]): The end date of the delivery window (latest projected delivery
            date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local
            time of the buyer. <br /> <br /> <span class="tablenote"> <b> Note: </b> For the best accuracy, always include
            the <code> contextualLocation</code> values in the <a href="/api-docs/buy/static/api-browse.html#Headers">
            <code>X-EBAY-C-ENDUSERCTX</code></a> request header.</span>
        min_estimated_delivery_date (Union[Unset, str]): The start date of the delivery window (earliest projected
            delivery date).  This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the
            local time of the buyer. <br /> <br /><span class="tablenote"> <b> Note: </b> For the best accuracy, always
            include the <code> contextualLocation</code> values in the <a href="/api-docs/buy/static/api-
            browse.html#Headers"> <code>X-EBAY-C-ENDUSERCTX</code></a> request header.</span>
        shipping_cost (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can provide
            the amount in both the currency used on the eBay site where an item is being offered and the conversion of that
            value into another currency, if applicable.
        shipping_cost_type (Union[Unset, str]): Indicates the type of shipping used to ship the item. Possible values
            are <code> FIXED</code> (flat-rate shipping) and <code> CALCULATED</code> (shipping cost calculated based on
            item and buyer location).
    """

    guaranteed_delivery: Union[Unset, bool] = UNSET
    max_estimated_delivery_date: Union[Unset, str] = UNSET
    min_estimated_delivery_date: Union[Unset, str] = UNSET
    shipping_cost: Union[Unset, ConvertedAmount] = UNSET
    shipping_cost_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guaranteed_delivery = self.guaranteed_delivery
        max_estimated_delivery_date = self.max_estimated_delivery_date
        min_estimated_delivery_date = self.min_estimated_delivery_date
        shipping_cost: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_cost, Unset):
            shipping_cost = self.shipping_cost.to_dict()

        shipping_cost_type = self.shipping_cost_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guaranteed_delivery is not UNSET:
            field_dict["guaranteedDelivery"] = guaranteed_delivery
        if max_estimated_delivery_date is not UNSET:
            field_dict["maxEstimatedDeliveryDate"] = max_estimated_delivery_date
        if min_estimated_delivery_date is not UNSET:
            field_dict["minEstimatedDeliveryDate"] = min_estimated_delivery_date
        if shipping_cost is not UNSET:
            field_dict["shippingCost"] = shipping_cost
        if shipping_cost_type is not UNSET:
            field_dict["shippingCostType"] = shipping_cost_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guaranteed_delivery = d.pop("guaranteedDelivery", UNSET)

        max_estimated_delivery_date = d.pop("maxEstimatedDeliveryDate", UNSET)

        min_estimated_delivery_date = d.pop("minEstimatedDeliveryDate", UNSET)

        _shipping_cost = d.pop("shippingCost", UNSET)
        shipping_cost: Union[Unset, ConvertedAmount]
        if isinstance(_shipping_cost, Unset):
            shipping_cost = UNSET
        else:
            shipping_cost = ConvertedAmount.from_dict(_shipping_cost)

        shipping_cost_type = d.pop("shippingCostType", UNSET)

        shipping_option_summary = cls(
            guaranteed_delivery=guaranteed_delivery,
            max_estimated_delivery_date=max_estimated_delivery_date,
            min_estimated_delivery_date=min_estimated_delivery_date,
            shipping_cost=shipping_cost,
            shipping_cost_type=shipping_cost_type,
        )

        shipping_option_summary.additional_properties = d
        return shipping_option_summary

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
