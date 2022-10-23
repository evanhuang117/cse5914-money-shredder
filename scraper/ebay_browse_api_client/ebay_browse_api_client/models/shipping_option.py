from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.converted_amount import ConvertedAmount
from ..models.ship_to_location import ShipToLocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShippingOption")


@attr.s(auto_attribs=True)
class ShippingOption:
    """The type that defines the fields for the details of a shipping provider.

    Attributes:
        additional_shipping_cost_per_unit (Union[Unset, ConvertedAmount]): This type defines the monetary value of an
            amount. It can provide the amount in both the currency used on the eBay site where an item is being offered and
            the conversion of that value into another currency, if applicable.
        cut_off_date_used_for_estimate (Union[Unset, str]): The deadline date that the item must be purchased by in
            order to be received by the buyer within the delivery window (<b> maxEstimatedDeliveryDate</b> and  <b>
            minEstimatedDeliveryDate</b> fields). This field is returned only for items that are eligible for 'Same Day
            Handling'. For these items, the value of this field is what is displayed in the <b> Delivery</b> line on the
            View Item page.  <br /><br />This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can
            convert into the local time of the buyer.
        fulfilled_through (Union[Unset, str]): If the item is being shipped by the eBay <a
            href="https://pages.ebay.com/seller-center/shipping/global-shipping-program.html ">Global Shipping program</a>,
            this field returns <code>GLOBAL_SHIPPING</code>.<br /><br />If the item is being shipped using the eBay
            International Shipping program, this field returns <code>INTERNATIONAL_SHIPPING</code>. <br /><br />Otherwise,
            this field is null. For implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/gct:FulfilledThroughEnum'>eBay API documentation</a>
        guaranteed_delivery (Union[Unset, bool]): Indicates if the seller has committed to shipping the item with eBay
            Guaranteed Delivery. With eBay Guaranteed Delivery, the  seller is committed to getting the line item to the
            buyer within 4 business days or less. See the <a href="https://www.ebay.com/help/buying/shipping-
            delivery/buying-items-ebay-guaranteed-delivery?id=4641 ">Buying items with eBay Guaranteed Delivery</a> help
            topic for more details about eBay Guaranteed Delivery.
        import_charges (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can
            provide the amount in both the currency used on the eBay site where an item is being offered and the conversion
            of that value into another currency, if applicable.
        max_estimated_delivery_date (Union[Unset, str]): The end date of the delivery window (latest projected delivery
            date).  This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the local
            time of the buyer. <br /> <br /> <span class="tablenote"> <b> Note: </b> For the best accuracy, always include
            the location of where the item is be shipped in the <code> contextualLocation</code> values of the <a
            href="/api-docs/buy/static/api-browse.html#Headers"> <code>X-EBAY-C-ENDUSERCTX</code></a> request header.</span>
        min_estimated_delivery_date (Union[Unset, str]): The start date of the delivery window (earliest projected
            delivery date). This value is returned in UTC format (yyyy-MM-ddThh:mm:ss.sssZ), which you can convert into the
            local time of the buyer. <br /> <br /><span class="tablenote"> <b> Note: </b> For the best accuracy, always
            include the location of where the item is be shipped in the <code> contextualLocation</code> values of the <a
            href="/api-docs/buy/static/api-browse.html#Headers"> <code>X-EBAY-C-ENDUSERCTX</code></a> request header.</span>
        quantity_used_for_estimate (Union[Unset, int]): The number of items used when calculating the estimation
            information.
        shipping_carrier_code (Union[Unset, str]): The name of the shipping provider, such as FedEx, or USPS.
        shipping_cost (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can provide
            the amount in both the currency used on the eBay site where an item is being offered and the conversion of that
            value into another currency, if applicable.
        shipping_cost_type (Union[Unset, str]): Indicates the class of the shipping cost. <br /><br /><b> Valid Values:
            </b> FIXED or CALCULATED <br /><br />Code so that your app gracefully handles any future changes to this list.
        shipping_service_code (Union[Unset, str]): The type of shipping service. For example, USPS First Class.
        ship_to_location_used_for_estimate (Union[Unset, ShipToLocation]): The type that defines the fields for the
            country and postal code of where an item is to be shipped.
        trademark_symbol (Union[Unset, str]): Any trademark symbol, such as &#8482; or &reg;, that needs to be shown in
            superscript next to the shipping service name.
        type (Union[Unset, str]): The type of a shipping option, such as EXPEDITED, ONE_DAY, STANDARD, ECONOMY, PICKUP,
            etc.
    """

    additional_shipping_cost_per_unit: Union[Unset, ConvertedAmount] = UNSET
    cut_off_date_used_for_estimate: Union[Unset, str] = UNSET
    fulfilled_through: Union[Unset, str] = UNSET
    guaranteed_delivery: Union[Unset, bool] = UNSET
    import_charges: Union[Unset, ConvertedAmount] = UNSET
    max_estimated_delivery_date: Union[Unset, str] = UNSET
    min_estimated_delivery_date: Union[Unset, str] = UNSET
    quantity_used_for_estimate: Union[Unset, int] = UNSET
    shipping_carrier_code: Union[Unset, str] = UNSET
    shipping_cost: Union[Unset, ConvertedAmount] = UNSET
    shipping_cost_type: Union[Unset, str] = UNSET
    shipping_service_code: Union[Unset, str] = UNSET
    ship_to_location_used_for_estimate: Union[Unset, ShipToLocation] = UNSET
    trademark_symbol: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_shipping_cost_per_unit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_shipping_cost_per_unit, Unset):
            additional_shipping_cost_per_unit = self.additional_shipping_cost_per_unit.to_dict()

        cut_off_date_used_for_estimate = self.cut_off_date_used_for_estimate
        fulfilled_through = self.fulfilled_through
        guaranteed_delivery = self.guaranteed_delivery
        import_charges: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.import_charges, Unset):
            import_charges = self.import_charges.to_dict()

        max_estimated_delivery_date = self.max_estimated_delivery_date
        min_estimated_delivery_date = self.min_estimated_delivery_date
        quantity_used_for_estimate = self.quantity_used_for_estimate
        shipping_carrier_code = self.shipping_carrier_code
        shipping_cost: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_cost, Unset):
            shipping_cost = self.shipping_cost.to_dict()

        shipping_cost_type = self.shipping_cost_type
        shipping_service_code = self.shipping_service_code
        ship_to_location_used_for_estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_location_used_for_estimate, Unset):
            ship_to_location_used_for_estimate = self.ship_to_location_used_for_estimate.to_dict()

        trademark_symbol = self.trademark_symbol
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_shipping_cost_per_unit is not UNSET:
            field_dict["additionalShippingCostPerUnit"] = additional_shipping_cost_per_unit
        if cut_off_date_used_for_estimate is not UNSET:
            field_dict["cutOffDateUsedForEstimate"] = cut_off_date_used_for_estimate
        if fulfilled_through is not UNSET:
            field_dict["fulfilledThrough"] = fulfilled_through
        if guaranteed_delivery is not UNSET:
            field_dict["guaranteedDelivery"] = guaranteed_delivery
        if import_charges is not UNSET:
            field_dict["importCharges"] = import_charges
        if max_estimated_delivery_date is not UNSET:
            field_dict["maxEstimatedDeliveryDate"] = max_estimated_delivery_date
        if min_estimated_delivery_date is not UNSET:
            field_dict["minEstimatedDeliveryDate"] = min_estimated_delivery_date
        if quantity_used_for_estimate is not UNSET:
            field_dict["quantityUsedForEstimate"] = quantity_used_for_estimate
        if shipping_carrier_code is not UNSET:
            field_dict["shippingCarrierCode"] = shipping_carrier_code
        if shipping_cost is not UNSET:
            field_dict["shippingCost"] = shipping_cost
        if shipping_cost_type is not UNSET:
            field_dict["shippingCostType"] = shipping_cost_type
        if shipping_service_code is not UNSET:
            field_dict["shippingServiceCode"] = shipping_service_code
        if ship_to_location_used_for_estimate is not UNSET:
            field_dict["shipToLocationUsedForEstimate"] = ship_to_location_used_for_estimate
        if trademark_symbol is not UNSET:
            field_dict["trademarkSymbol"] = trademark_symbol
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _additional_shipping_cost_per_unit = d.pop("additionalShippingCostPerUnit", UNSET)
        additional_shipping_cost_per_unit: Union[Unset, ConvertedAmount]
        if isinstance(_additional_shipping_cost_per_unit, Unset):
            additional_shipping_cost_per_unit = UNSET
        else:
            additional_shipping_cost_per_unit = ConvertedAmount.from_dict(_additional_shipping_cost_per_unit)

        cut_off_date_used_for_estimate = d.pop("cutOffDateUsedForEstimate", UNSET)

        fulfilled_through = d.pop("fulfilledThrough", UNSET)

        guaranteed_delivery = d.pop("guaranteedDelivery", UNSET)

        _import_charges = d.pop("importCharges", UNSET)
        import_charges: Union[Unset, ConvertedAmount]
        if isinstance(_import_charges, Unset):
            import_charges = UNSET
        else:
            import_charges = ConvertedAmount.from_dict(_import_charges)

        max_estimated_delivery_date = d.pop("maxEstimatedDeliveryDate", UNSET)

        min_estimated_delivery_date = d.pop("minEstimatedDeliveryDate", UNSET)

        quantity_used_for_estimate = d.pop("quantityUsedForEstimate", UNSET)

        shipping_carrier_code = d.pop("shippingCarrierCode", UNSET)

        _shipping_cost = d.pop("shippingCost", UNSET)
        shipping_cost: Union[Unset, ConvertedAmount]
        if isinstance(_shipping_cost, Unset):
            shipping_cost = UNSET
        else:
            shipping_cost = ConvertedAmount.from_dict(_shipping_cost)

        shipping_cost_type = d.pop("shippingCostType", UNSET)

        shipping_service_code = d.pop("shippingServiceCode", UNSET)

        _ship_to_location_used_for_estimate = d.pop("shipToLocationUsedForEstimate", UNSET)
        ship_to_location_used_for_estimate: Union[Unset, ShipToLocation]
        if isinstance(_ship_to_location_used_for_estimate, Unset):
            ship_to_location_used_for_estimate = UNSET
        else:
            ship_to_location_used_for_estimate = ShipToLocation.from_dict(_ship_to_location_used_for_estimate)

        trademark_symbol = d.pop("trademarkSymbol", UNSET)

        type = d.pop("type", UNSET)

        shipping_option = cls(
            additional_shipping_cost_per_unit=additional_shipping_cost_per_unit,
            cut_off_date_used_for_estimate=cut_off_date_used_for_estimate,
            fulfilled_through=fulfilled_through,
            guaranteed_delivery=guaranteed_delivery,
            import_charges=import_charges,
            max_estimated_delivery_date=max_estimated_delivery_date,
            min_estimated_delivery_date=min_estimated_delivery_date,
            quantity_used_for_estimate=quantity_used_for_estimate,
            shipping_carrier_code=shipping_carrier_code,
            shipping_cost=shipping_cost,
            shipping_cost_type=shipping_cost_type,
            shipping_service_code=shipping_service_code,
            ship_to_location_used_for_estimate=ship_to_location_used_for_estimate,
            trademark_symbol=trademark_symbol,
            type=type,
        )

        shipping_option.additional_properties = d
        return shipping_option

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
