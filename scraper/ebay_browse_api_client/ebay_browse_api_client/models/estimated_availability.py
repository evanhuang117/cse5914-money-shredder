from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EstimatedAvailability")


@attr.s(auto_attribs=True)
class EstimatedAvailability:
    """The type that defines the fields for the estimated item availability information.

    Attributes:
        availability_threshold (Union[Unset, int]): This field is return only when the seller sets their '<a
            href="#display-item-quantity">display item quantity</a>' preference to <b> Display "More than 10 available" in
            your listing (if applicable)</b>. The value of this field will be "10", which is the threshold value. <br /><br
            />Code so that your app gracefully handles any future changes to this value.
        availability_threshold_type (Union[Unset, str]): <a name="display-item-quantity"></a> This field is return only
            when the seller sets their <b> Display Item Quantity</b> preference to <b> Display "More than 10 available" in
            your listing (if applicable)</b>. The value of this field will be <code> MORE_THAN</code>. This indicates that
            the seller has more than the 'quantity display preference', which is 10, in stock for this item.    <br /><br />
            The following are the display item quantity preferences the seller can set. <br /><ul><li> <b> Display "More
            than 10 available" in your listing (if applicable) </b><ul> <li>If the seller enables this preference, this
            field is returned as long as there are more than 10 of this item in inventory.</li>  <li> If the quantity is
            equal to 10 or drops below 10, this field is not returned and the estimated quantity of the item is returned in
            the <b> estimatedAvailableQuantity</b> field.</li></ul> </li> <li> <b> Display the exact quantity in your
            items</b> <br />If the seller enables this preference, the <b> availabilityThresholdType</b> and <b>
            availabilityThreshold</b> fields are not returned and the estimated quantity of the item is returned in the <b>
            estimatedAvailableQuantity</b> field.<br /><br /><b> Note: </b> Because the quantity of an item can change
            several times within a second, it is impossible to return the exact quantity. </li></ul>   <br />Code so that
            your app gracefully handles any future changes to these preferences. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AvailabilityThresholdEnum'>eBay API
            documentation</a>
        delivery_options (Union[Unset, List[str]]): An array of available delivery options. <br><br><b> Valid Values:
            </b> SHIP_TO_HOME, SELLER_ARRANGED_LOCAL_PICKUP, IN_STORE_PICKUP, PICKUP_DROP_OFF, or DIGITAL_DELIVERY <br /><br
            />Code so that your app gracefully handles any future changes to this list.
        estimated_availability_status (Union[Unset, str]): An enumeration value representing the inventory status of
            this item.<br /><br /><span class="tablenote"><b> Note: </b>Be sure to review the <b>itemEndDate</b> field to
            determine whether the item is available for purchase.</span><br><br><b> Valid Values: </b> IN_STOCK,
            LIMITED_STOCK, or OUT_OF_STOCK <br /><br />Code so that your app gracefully handles any future changes to this
            list. For implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/gct:AvailabilityStatusEnum'>eBay API documentation</a>
        estimated_available_quantity (Union[Unset, int]): The estimated number of this item that are available for
            purchase. Because the quantity of an item can change several times within a second, it is impossible to return
            the exact quantity. So instead of returning quantity, the estimated availability of the item is returned.
        estimated_sold_quantity (Union[Unset, int]): The estimated number of this item that have been sold.
    """

    availability_threshold: Union[Unset, int] = UNSET
    availability_threshold_type: Union[Unset, str] = UNSET
    delivery_options: Union[Unset, List[str]] = UNSET
    estimated_availability_status: Union[Unset, str] = UNSET
    estimated_available_quantity: Union[Unset, int] = UNSET
    estimated_sold_quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        availability_threshold = self.availability_threshold
        availability_threshold_type = self.availability_threshold_type
        delivery_options: Union[Unset, List[str]] = UNSET
        if not isinstance(self.delivery_options, Unset):
            delivery_options = self.delivery_options

        estimated_availability_status = self.estimated_availability_status
        estimated_available_quantity = self.estimated_available_quantity
        estimated_sold_quantity = self.estimated_sold_quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_threshold is not UNSET:
            field_dict["availabilityThreshold"] = availability_threshold
        if availability_threshold_type is not UNSET:
            field_dict["availabilityThresholdType"] = availability_threshold_type
        if delivery_options is not UNSET:
            field_dict["deliveryOptions"] = delivery_options
        if estimated_availability_status is not UNSET:
            field_dict["estimatedAvailabilityStatus"] = estimated_availability_status
        if estimated_available_quantity is not UNSET:
            field_dict["estimatedAvailableQuantity"] = estimated_available_quantity
        if estimated_sold_quantity is not UNSET:
            field_dict["estimatedSoldQuantity"] = estimated_sold_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        availability_threshold = d.pop("availabilityThreshold", UNSET)

        availability_threshold_type = d.pop("availabilityThresholdType", UNSET)

        delivery_options = cast(List[str], d.pop("deliveryOptions", UNSET))

        estimated_availability_status = d.pop("estimatedAvailabilityStatus", UNSET)

        estimated_available_quantity = d.pop("estimatedAvailableQuantity", UNSET)

        estimated_sold_quantity = d.pop("estimatedSoldQuantity", UNSET)

        estimated_availability = cls(
            availability_threshold=availability_threshold,
            availability_threshold_type=availability_threshold_type,
            delivery_options=delivery_options,
            estimated_availability_status=estimated_availability_status,
            estimated_available_quantity=estimated_available_quantity,
            estimated_sold_quantity=estimated_sold_quantity,
        )

        estimated_availability.additional_properties = d
        return estimated_availability

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
