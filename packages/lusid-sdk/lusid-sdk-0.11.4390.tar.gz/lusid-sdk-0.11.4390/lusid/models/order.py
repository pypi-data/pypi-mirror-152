# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4390
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class Order(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'properties': 'dict(str, PerpetualProperty)',
        'version': 'Version',
        'instrument_identifiers': 'dict(str, str)',
        'quantity': 'int',
        'side': 'str',
        'order_book_id': 'ResourceId',
        'portfolio_id': 'ResourceId',
        'id': 'ResourceId',
        'instrument_scope': 'str',
        'lusid_instrument_id': 'str',
        'state': 'str',
        'type': 'str',
        'time_in_force': 'str',
        'date': 'datetime',
        'price': 'CurrencyAndAmount',
        'order_instruction_id': 'ResourceId',
        'package_id': 'ResourceId',
        'links': 'list[Link]'
    }

    attribute_map = {
        'properties': 'properties',
        'version': 'version',
        'instrument_identifiers': 'instrumentIdentifiers',
        'quantity': 'quantity',
        'side': 'side',
        'order_book_id': 'orderBookId',
        'portfolio_id': 'portfolioId',
        'id': 'id',
        'instrument_scope': 'instrumentScope',
        'lusid_instrument_id': 'lusidInstrumentId',
        'state': 'state',
        'type': 'type',
        'time_in_force': 'timeInForce',
        'date': 'date',
        'price': 'price',
        'order_instruction_id': 'orderInstructionId',
        'package_id': 'packageId',
        'links': 'links'
    }

    required_map = {
        'properties': 'optional',
        'version': 'optional',
        'instrument_identifiers': 'required',
        'quantity': 'required',
        'side': 'required',
        'order_book_id': 'optional',
        'portfolio_id': 'required',
        'id': 'required',
        'instrument_scope': 'optional',
        'lusid_instrument_id': 'required',
        'state': 'optional',
        'type': 'optional',
        'time_in_force': 'optional',
        'date': 'optional',
        'price': 'optional',
        'order_instruction_id': 'optional',
        'package_id': 'optional',
        'links': 'optional'
    }

    def __init__(self, properties=None, version=None, instrument_identifiers=None, quantity=None, side=None, order_book_id=None, portfolio_id=None, id=None, instrument_scope=None, lusid_instrument_id=None, state=None, type=None, time_in_force=None, date=None, price=None, order_instruction_id=None, package_id=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Order - a model defined in OpenAPI"
        
        :param properties:  Client-defined properties associated with this order.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param version: 
        :type version: lusid.Version
        :param instrument_identifiers:  The instrument ordered. (required)
        :type instrument_identifiers: dict(str, str)
        :param quantity:  The quantity of given instrument ordered. (required)
        :type quantity: int
        :param side:  The client's representation of the order's side (buy, sell, short, etc) (required)
        :type side: str
        :param order_book_id: 
        :type order_book_id: lusid.ResourceId
        :param portfolio_id:  (required)
        :type portfolio_id: lusid.ResourceId
        :param id:  (required)
        :type id: lusid.ResourceId
        :param instrument_scope:  The scope in which the instrument lies
        :type instrument_scope: str
        :param lusid_instrument_id:  The LUSID instrument id for the instrument ordered. (required)
        :type lusid_instrument_id: str
        :param state:  The order's state (examples: New, PartiallyFilled, ...)
        :type state: str
        :param type:  The order's type (examples: Limit, Market, ...)
        :type type: str
        :param time_in_force:  The order's time in force (examples: Day, GoodTilCancel, ...)
        :type time_in_force: str
        :param date:  The date on which the order was made
        :type date: datetime
        :param price: 
        :type price: lusid.CurrencyAndAmount
        :param order_instruction_id: 
        :type order_instruction_id: lusid.ResourceId
        :param package_id: 
        :type package_id: lusid.ResourceId
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._properties = None
        self._version = None
        self._instrument_identifiers = None
        self._quantity = None
        self._side = None
        self._order_book_id = None
        self._portfolio_id = None
        self._id = None
        self._instrument_scope = None
        self._lusid_instrument_id = None
        self._state = None
        self._type = None
        self._time_in_force = None
        self._date = None
        self._price = None
        self._order_instruction_id = None
        self._package_id = None
        self._links = None
        self.discriminator = None

        self.properties = properties
        if version is not None:
            self.version = version
        self.instrument_identifiers = instrument_identifiers
        self.quantity = quantity
        self.side = side
        if order_book_id is not None:
            self.order_book_id = order_book_id
        self.portfolio_id = portfolio_id
        self.id = id
        self.instrument_scope = instrument_scope
        self.lusid_instrument_id = lusid_instrument_id
        self.state = state
        self.type = type
        self.time_in_force = time_in_force
        if date is not None:
            self.date = date
        if price is not None:
            self.price = price
        if order_instruction_id is not None:
            self.order_instruction_id = order_instruction_id
        if package_id is not None:
            self.package_id = package_id
        self.links = links

    @property
    def properties(self):
        """Gets the properties of this Order.  # noqa: E501

        Client-defined properties associated with this order.  # noqa: E501

        :return: The properties of this Order.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Order.

        Client-defined properties associated with this order.  # noqa: E501

        :param properties: The properties of this Order.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def version(self):
        """Gets the version of this Order.  # noqa: E501


        :return: The version of this Order.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Order.


        :param version: The version of this Order.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this Order.  # noqa: E501

        The instrument ordered.  # noqa: E501

        :return: The instrument_identifiers of this Order.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this Order.

        The instrument ordered.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this Order.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def quantity(self):
        """Gets the quantity of this Order.  # noqa: E501

        The quantity of given instrument ordered.  # noqa: E501

        :return: The quantity of this Order.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Order.

        The quantity of given instrument ordered.  # noqa: E501

        :param quantity: The quantity of this Order.  # noqa: E501
        :type quantity: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def side(self):
        """Gets the side of this Order.  # noqa: E501

        The client's representation of the order's side (buy, sell, short, etc)  # noqa: E501

        :return: The side of this Order.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Order.

        The client's representation of the order's side (buy, sell, short, etc)  # noqa: E501

        :param side: The side of this Order.  # noqa: E501
        :type side: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def order_book_id(self):
        """Gets the order_book_id of this Order.  # noqa: E501


        :return: The order_book_id of this Order.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._order_book_id

    @order_book_id.setter
    def order_book_id(self, order_book_id):
        """Sets the order_book_id of this Order.


        :param order_book_id: The order_book_id of this Order.  # noqa: E501
        :type order_book_id: lusid.ResourceId
        """

        self._order_book_id = order_book_id

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this Order.  # noqa: E501


        :return: The portfolio_id of this Order.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this Order.


        :param portfolio_id: The portfolio_id of this Order.  # noqa: E501
        :type portfolio_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and portfolio_id is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_id`, must not be `None`")  # noqa: E501

        self._portfolio_id = portfolio_id

    @property
    def id(self):
        """Gets the id of this Order.  # noqa: E501


        :return: The id of this Order.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        :param id: The id of this Order.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def instrument_scope(self):
        """Gets the instrument_scope of this Order.  # noqa: E501

        The scope in which the instrument lies  # noqa: E501

        :return: The instrument_scope of this Order.  # noqa: E501
        :rtype: str
        """
        return self._instrument_scope

    @instrument_scope.setter
    def instrument_scope(self, instrument_scope):
        """Sets the instrument_scope of this Order.

        The scope in which the instrument lies  # noqa: E501

        :param instrument_scope: The instrument_scope of this Order.  # noqa: E501
        :type instrument_scope: str
        """

        self._instrument_scope = instrument_scope

    @property
    def lusid_instrument_id(self):
        """Gets the lusid_instrument_id of this Order.  # noqa: E501

        The LUSID instrument id for the instrument ordered.  # noqa: E501

        :return: The lusid_instrument_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._lusid_instrument_id

    @lusid_instrument_id.setter
    def lusid_instrument_id(self, lusid_instrument_id):
        """Sets the lusid_instrument_id of this Order.

        The LUSID instrument id for the instrument ordered.  # noqa: E501

        :param lusid_instrument_id: The lusid_instrument_id of this Order.  # noqa: E501
        :type lusid_instrument_id: str
        """
        if self.local_vars_configuration.client_side_validation and lusid_instrument_id is None:  # noqa: E501
            raise ValueError("Invalid value for `lusid_instrument_id`, must not be `None`")  # noqa: E501

        self._lusid_instrument_id = lusid_instrument_id

    @property
    def state(self):
        """Gets the state of this Order.  # noqa: E501

        The order's state (examples: New, PartiallyFilled, ...)  # noqa: E501

        :return: The state of this Order.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Order.

        The order's state (examples: New, PartiallyFilled, ...)  # noqa: E501

        :param state: The state of this Order.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def type(self):
        """Gets the type of this Order.  # noqa: E501

        The order's type (examples: Limit, Market, ...)  # noqa: E501

        :return: The type of this Order.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Order.

        The order's type (examples: Limit, Market, ...)  # noqa: E501

        :param type: The type of this Order.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def time_in_force(self):
        """Gets the time_in_force of this Order.  # noqa: E501

        The order's time in force (examples: Day, GoodTilCancel, ...)  # noqa: E501

        :return: The time_in_force of this Order.  # noqa: E501
        :rtype: str
        """
        return self._time_in_force

    @time_in_force.setter
    def time_in_force(self, time_in_force):
        """Sets the time_in_force of this Order.

        The order's time in force (examples: Day, GoodTilCancel, ...)  # noqa: E501

        :param time_in_force: The time_in_force of this Order.  # noqa: E501
        :type time_in_force: str
        """

        self._time_in_force = time_in_force

    @property
    def date(self):
        """Gets the date of this Order.  # noqa: E501

        The date on which the order was made  # noqa: E501

        :return: The date of this Order.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Order.

        The date on which the order was made  # noqa: E501

        :param date: The date of this Order.  # noqa: E501
        :type date: datetime
        """

        self._date = date

    @property
    def price(self):
        """Gets the price of this Order.  # noqa: E501


        :return: The price of this Order.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Order.


        :param price: The price of this Order.  # noqa: E501
        :type price: lusid.CurrencyAndAmount
        """

        self._price = price

    @property
    def order_instruction_id(self):
        """Gets the order_instruction_id of this Order.  # noqa: E501


        :return: The order_instruction_id of this Order.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._order_instruction_id

    @order_instruction_id.setter
    def order_instruction_id(self, order_instruction_id):
        """Sets the order_instruction_id of this Order.


        :param order_instruction_id: The order_instruction_id of this Order.  # noqa: E501
        :type order_instruction_id: lusid.ResourceId
        """

        self._order_instruction_id = order_instruction_id

    @property
    def package_id(self):
        """Gets the package_id of this Order.  # noqa: E501


        :return: The package_id of this Order.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this Order.


        :param package_id: The package_id of this Order.  # noqa: E501
        :type package_id: lusid.ResourceId
        """

        self._package_id = package_id

    @property
    def links(self):
        """Gets the links of this Order.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this Order.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Order.

        Collection of links.  # noqa: E501

        :param links: The links of this Order.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()
