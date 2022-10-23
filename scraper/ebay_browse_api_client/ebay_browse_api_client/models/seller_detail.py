from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.seller_legal_info import SellerLegalInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="SellerDetail")


@attr.s(auto_attribs=True)
class SellerDetail:
    """The type that defines the fields for basic and detailed information about the seller of the item returned by the <b>
    item</b> resource.

        Attributes:
            feedback_percentage (Union[Unset, str]): The percentage of the total positive feedback.
            feedback_score (Union[Unset, int]): The feedback score of the seller. This value is based on the ratings from
                eBay members that bought items from this seller.
            seller_account_type (Union[Unset, str]): This indicates if the seller is a business or an individual. This is
                determined when the seller registers with eBay. If they register for a business account, this value will be
                BUSINESS. If they register for a private account, this value will be INDIVIDUAL. This designation is required by
                the tax laws in the following countries:  <br /><br /> This field is returned only on the following sites. <br
                /><br />EBAY_AT, EBAY_BE, EBAY_CH, EBAY_DE, EBAY_ES, EBAY_FR, EBAY_GB, EBAY_IE, EBAY_IT, EBAY_PL <br /><br /><b>
                Valid Values:</b> BUSINESS or INDIVIDUAL <br /><br />Code so that your app gracefully handles any future changes
                to this list.
            seller_legal_info (Union[Unset, SellerLegalInfo]): The type that defines the fields for the contact information
                for a seller.
            username (Union[Unset, str]): The user name created by the seller for use on eBay.
    """

    feedback_percentage: Union[Unset, str] = UNSET
    feedback_score: Union[Unset, int] = UNSET
    seller_account_type: Union[Unset, str] = UNSET
    seller_legal_info: Union[Unset, SellerLegalInfo] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feedback_percentage = self.feedback_percentage
        feedback_score = self.feedback_score
        seller_account_type = self.seller_account_type
        seller_legal_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_legal_info, Unset):
            seller_legal_info = self.seller_legal_info.to_dict()

        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feedback_percentage is not UNSET:
            field_dict["feedbackPercentage"] = feedback_percentage
        if feedback_score is not UNSET:
            field_dict["feedbackScore"] = feedback_score
        if seller_account_type is not UNSET:
            field_dict["sellerAccountType"] = seller_account_type
        if seller_legal_info is not UNSET:
            field_dict["sellerLegalInfo"] = seller_legal_info
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feedback_percentage = d.pop("feedbackPercentage", UNSET)

        feedback_score = d.pop("feedbackScore", UNSET)

        seller_account_type = d.pop("sellerAccountType", UNSET)

        _seller_legal_info = d.pop("sellerLegalInfo", UNSET)
        seller_legal_info: Union[Unset, SellerLegalInfo]
        if isinstance(_seller_legal_info, Unset):
            seller_legal_info = UNSET
        else:
            seller_legal_info = SellerLegalInfo.from_dict(_seller_legal_info)

        username = d.pop("username", UNSET)

        seller_detail = cls(
            feedback_percentage=feedback_percentage,
            feedback_score=feedback_score,
            seller_account_type=seller_account_type,
            seller_legal_info=seller_legal_info,
            username=username,
        )

        seller_detail.additional_properties = d
        return seller_detail

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
