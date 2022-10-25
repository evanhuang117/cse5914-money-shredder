from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.time_duration import TimeDuration
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemReturnTerms")


@attr.s(auto_attribs=True)
class ItemReturnTerms:
    """The type that defines the fields for the seller's return policy.

    Attributes:
        extended_holiday_returns_offered (Union[Unset, bool]): This indicates if the seller has enabled the Extended
            Holiday Returns feature on the item. Extended Holiday Returns are only applicable during the US holiday season,
            and gives buyers extra time to return an item. This 'extra time' will typically extend beyond what is set
            through the <b> returnPeriod</b> value.
        refund_method (Union[Unset, str]): An enumeration value that indicates how a buyer is refunded when an item is
            returned. <br><br><b> Valid Values: </b> MONEY_BACK or MERCHANDISE_CREDIT  <br /><br />Code so that your app
            gracefully handles any future changes to this list. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/gct:RefundMethodEnum'>eBay API documentation</a>
        restocking_fee_percentage (Union[Unset, str]): This string field indicates the restocking fee percentage that
            the seller has set on the item. Sellers have the option of setting no restocking fee for an item, or they can
            set the percentage to 10, 15, or 20 percent. So, if the cost of the item was $100, and the restocking percentage
            was 20 percent, the buyer would be charged $20 to return that item, so instead of receiving a $100 refund, they
            would receive $80 due to the restocking fee.
        return_instructions (Union[Unset, str]): Text written by the seller describing what the buyer needs to do in
            order to return the item.
        return_method (Union[Unset, str]): An enumeration value that indicates the alternative methods for a full refund
            when an item is returned. This field is returned if the seller offers the buyer an item replacement or exchange
            instead of a monetary refund. <br><br><b> Valid Values: </b>  <ul><li><b> REPLACEMENT</b> -  Indicates that the
            buyer has the option of receiving money back for the returned item, or they can choose to have the seller
            replace the item with an identical item.</li>  <li><b> EXCHANGE</b> - Indicates that the buyer has the option of
            receiving money back for the returned item, or they can exchange the item for another similar item.</li></ul>
            Code so that your app gracefully handles any future changes to this list. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/gct:ReturnMethodEnum'>eBay API documentation</a>
        return_period (Union[Unset, TimeDuration]): The type that defines the fields for a period of time in the time-
            measurement units supplied.
        returns_accepted (Union[Unset, bool]): Indicates whether the seller accepts returns for the item.
        return_shipping_cost_payer (Union[Unset, str]): This enumeration value indicates whether the buyer or seller is
            responsible for return shipping costs when an item is returned. <br><br><b> Valid Values: </b> <ul><li><b>
            SELLER</b> - Indicates the seller will pay for the shipping costs to return the item.</li>  <li><b> BUYER</b> -
            Indicates the buyer will pay for the shipping costs to return the item.</li>  </ul>  Code so that your app
            gracefully handles any future changes to this list. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/gct:ReturnShippingCostPayerEnum'>eBay API
            documentation</a>
    """

    extended_holiday_returns_offered: Union[Unset, bool] = UNSET
    refund_method: Union[Unset, str] = UNSET
    restocking_fee_percentage: Union[Unset, str] = UNSET
    return_instructions: Union[Unset, str] = UNSET
    return_method: Union[Unset, str] = UNSET
    return_period: Union[Unset, TimeDuration] = UNSET
    returns_accepted: Union[Unset, bool] = UNSET
    return_shipping_cost_payer: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extended_holiday_returns_offered = self.extended_holiday_returns_offered
        refund_method = self.refund_method
        restocking_fee_percentage = self.restocking_fee_percentage
        return_instructions = self.return_instructions
        return_method = self.return_method
        return_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_period, Unset):
            return_period = self.return_period.to_dict()

        returns_accepted = self.returns_accepted
        return_shipping_cost_payer = self.return_shipping_cost_payer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extended_holiday_returns_offered is not UNSET:
            field_dict["extendedHolidayReturnsOffered"] = extended_holiday_returns_offered
        if refund_method is not UNSET:
            field_dict["refundMethod"] = refund_method
        if restocking_fee_percentage is not UNSET:
            field_dict["restockingFeePercentage"] = restocking_fee_percentage
        if return_instructions is not UNSET:
            field_dict["returnInstructions"] = return_instructions
        if return_method is not UNSET:
            field_dict["returnMethod"] = return_method
        if return_period is not UNSET:
            field_dict["returnPeriod"] = return_period
        if returns_accepted is not UNSET:
            field_dict["returnsAccepted"] = returns_accepted
        if return_shipping_cost_payer is not UNSET:
            field_dict["returnShippingCostPayer"] = return_shipping_cost_payer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        extended_holiday_returns_offered = d.pop("extendedHolidayReturnsOffered", UNSET)

        refund_method = d.pop("refundMethod", UNSET)

        restocking_fee_percentage = d.pop("restockingFeePercentage", UNSET)

        return_instructions = d.pop("returnInstructions", UNSET)

        return_method = d.pop("returnMethod", UNSET)

        _return_period = d.pop("returnPeriod", UNSET)
        return_period: Union[Unset, TimeDuration]
        if isinstance(_return_period, Unset):
            return_period = UNSET
        else:
            return_period = TimeDuration.from_dict(_return_period)

        returns_accepted = d.pop("returnsAccepted", UNSET)

        return_shipping_cost_payer = d.pop("returnShippingCostPayer", UNSET)

        item_return_terms = cls(
            extended_holiday_returns_offered=extended_holiday_returns_offered,
            refund_method=refund_method,
            restocking_fee_percentage=restocking_fee_percentage,
            return_instructions=return_instructions,
            return_method=return_method,
            return_period=return_period,
            returns_accepted=returns_accepted,
            return_shipping_cost_payer=return_shipping_cost_payer,
        )

        item_return_terms.additional_properties = d
        return item_return_terms

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
