from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.legal_address import LegalAddress
from ..models.vat_detail import VatDetail
from ..types import UNSET, Unset

T = TypeVar("T", bound="SellerLegalInfo")


@attr.s(auto_attribs=True)
class SellerLegalInfo:
    """The type that defines the fields for the contact information for a seller.

    Attributes:
        email (Union[Unset, str]): The seller's business email address.
        fax (Union[Unset, str]): The seller' business fax number.
        imprint (Union[Unset, str]): This is a free-form string created by the seller. This is information often found
            on business cards, such as address. This is information used by some countries.
        legal_contact_first_name (Union[Unset, str]): The seller's first name.
        legal_contact_last_name (Union[Unset, str]): The seller's last name.
        name (Union[Unset, str]): The name of the seller's business.
        phone (Union[Unset, str]): The seller's business phone number.
        registration_number (Union[Unset, str]): The seller's registration number. This is information used by some
            countries.
        seller_provided_legal_address (Union[Unset, LegalAddress]): Type that defines the fields for the seller's
            address.
        terms_of_service (Union[Unset, str]): This is a free-form string created by the seller. This is the seller's
            terms or condition, which is in addition to the seller's return policies.
        vat_details (Union[Unset, List[VatDetail]]): An array of the seller's VAT (value added tax) IDs and the issuing
            country. VAT is a tax added by some European countries.
    """

    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    imprint: Union[Unset, str] = UNSET
    legal_contact_first_name: Union[Unset, str] = UNSET
    legal_contact_last_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    registration_number: Union[Unset, str] = UNSET
    seller_provided_legal_address: Union[Unset, LegalAddress] = UNSET
    terms_of_service: Union[Unset, str] = UNSET
    vat_details: Union[Unset, List[VatDetail]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        fax = self.fax
        imprint = self.imprint
        legal_contact_first_name = self.legal_contact_first_name
        legal_contact_last_name = self.legal_contact_last_name
        name = self.name
        phone = self.phone
        registration_number = self.registration_number
        seller_provided_legal_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.seller_provided_legal_address, Unset):
            seller_provided_legal_address = self.seller_provided_legal_address.to_dict()

        terms_of_service = self.terms_of_service
        vat_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vat_details, Unset):
            vat_details = []
            for vat_details_item_data in self.vat_details:
                vat_details_item = vat_details_item_data.to_dict()

                vat_details.append(vat_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if imprint is not UNSET:
            field_dict["imprint"] = imprint
        if legal_contact_first_name is not UNSET:
            field_dict["legalContactFirstName"] = legal_contact_first_name
        if legal_contact_last_name is not UNSET:
            field_dict["legalContactLastName"] = legal_contact_last_name
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if registration_number is not UNSET:
            field_dict["registrationNumber"] = registration_number
        if seller_provided_legal_address is not UNSET:
            field_dict["sellerProvidedLegalAddress"] = seller_provided_legal_address
        if terms_of_service is not UNSET:
            field_dict["termsOfService"] = terms_of_service
        if vat_details is not UNSET:
            field_dict["vatDetails"] = vat_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        imprint = d.pop("imprint", UNSET)

        legal_contact_first_name = d.pop("legalContactFirstName", UNSET)

        legal_contact_last_name = d.pop("legalContactLastName", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        registration_number = d.pop("registrationNumber", UNSET)

        _seller_provided_legal_address = d.pop("sellerProvidedLegalAddress", UNSET)
        seller_provided_legal_address: Union[Unset, LegalAddress]
        if isinstance(_seller_provided_legal_address, Unset):
            seller_provided_legal_address = UNSET
        else:
            seller_provided_legal_address = LegalAddress.from_dict(_seller_provided_legal_address)

        terms_of_service = d.pop("termsOfService", UNSET)

        vat_details = []
        _vat_details = d.pop("vatDetails", UNSET)
        for vat_details_item_data in _vat_details or []:
            vat_details_item = VatDetail.from_dict(vat_details_item_data)

            vat_details.append(vat_details_item)

        seller_legal_info = cls(
            email=email,
            fax=fax,
            imprint=imprint,
            legal_contact_first_name=legal_contact_first_name,
            legal_contact_last_name=legal_contact_last_name,
            name=name,
            phone=phone,
            registration_number=registration_number,
            seller_provided_legal_address=seller_provided_legal_address,
            terms_of_service=terms_of_service,
            vat_details=vat_details,
        )

        seller_legal_info.additional_properties = d
        return seller_legal_info

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
