from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.product_identity import ProductIdentity
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdditionalProductIdentity")


@attr.s(auto_attribs=True)
class AdditionalProductIdentity:
    """The type that defines the array of product identifiers associated with the item. This container is returned if the
    seller has associated the eBay Product Identifier (ePID) with the item and in the request <b> fieldgroups</b> is set
    to <code>PRODUCT</code>.

        Attributes:
            product_identity (Union[Unset, List[ProductIdentity]]): An array of the product identifier/value pairs for the
                product associated with the item. This is returned if the seller has associated the eBay Product Identifier
                (ePID) with the item and the request has <b> fieldgroups</b> set to <code>PRODUCT</code>. <br /><br />The
                following table shows what is returned, based on the item information provided by the seller, when the <b>
                fieldgroups</b> set to <code>PRODUCT</code>.        <br /><br /><div style="overflow-x:auto;"> <table border=1>
                <tr> <th> ePID Provided </th>  <th> Product&nbsp;ID(s) Provided</th> <th> Response</th> </tr> <tr> <td> No </td>
                <td> No </td> <td> The <b> AdditionalProductIdentity</b> container is <i> not</i> returned.</td></tr>   <tr>
                <td> No </td>  <td> Yes </td>  <td> The <b> AdditionalProductIdentity</b> container is <i> not</i> returned but
                the product identifiers specified by the seller are returned in the <b> localizedAspects</b> container. </td>
                </tr>   <tr> <td> Yes </td>  <td> No </td> <td>  The <b> AdditionalProductIdentity</b> container is returned
                listing the product identifiers of the product.</td></tr>   <tr> <td> Yes </td>  <td> Yes </td> <td> The <b>
                AdditionalProductIdentity</b> container is returned listing all the product identifiers of the product and the
                product identifiers specified by the seller are returned in the <b> localizedAspects</b> container.</td> </tr>
                </table> </div>
    """

    product_identity: Union[Unset, List[ProductIdentity]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_identity: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_identity, Unset):
            product_identity = []
            for product_identity_item_data in self.product_identity:
                product_identity_item = product_identity_item_data.to_dict()

                product_identity.append(product_identity_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_identity is not UNSET:
            field_dict["productIdentity"] = product_identity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_identity = []
        _product_identity = d.pop("productIdentity", UNSET)
        for product_identity_item_data in _product_identity or []:
            product_identity_item = ProductIdentity.from_dict(product_identity_item_data)

            product_identity.append(product_identity_item)

        additional_product_identity = cls(
            product_identity=product_identity,
        )

        additional_product_identity.additional_properties = d
        return additional_product_identity

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
