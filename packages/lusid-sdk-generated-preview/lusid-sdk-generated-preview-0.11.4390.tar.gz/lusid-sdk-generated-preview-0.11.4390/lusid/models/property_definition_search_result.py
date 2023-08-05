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


class PropertyDefinitionSearchResult(object):
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
        'href': 'str',
        'key': 'str',
        'value_type': 'str',
        'display_name': 'str',
        'data_type_id': 'ResourceId',
        'type': 'str',
        'unit_schema': 'str',
        'domain': 'str',
        'scope': 'str',
        'code': 'str',
        'value_required': 'bool',
        'life_time': 'str',
        'constraint_style': 'str',
        'property_definition_type': 'str',
        'property_description': 'str',
        'derivation_formula': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'key': 'key',
        'value_type': 'valueType',
        'display_name': 'displayName',
        'data_type_id': 'dataTypeId',
        'type': 'type',
        'unit_schema': 'unitSchema',
        'domain': 'domain',
        'scope': 'scope',
        'code': 'code',
        'value_required': 'valueRequired',
        'life_time': 'lifeTime',
        'constraint_style': 'constraintStyle',
        'property_definition_type': 'propertyDefinitionType',
        'property_description': 'propertyDescription',
        'derivation_formula': 'derivationFormula',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'key': 'optional',
        'value_type': 'optional',
        'display_name': 'optional',
        'data_type_id': 'optional',
        'type': 'optional',
        'unit_schema': 'optional',
        'domain': 'optional',
        'scope': 'optional',
        'code': 'optional',
        'value_required': 'optional',
        'life_time': 'optional',
        'constraint_style': 'optional',
        'property_definition_type': 'optional',
        'property_description': 'optional',
        'derivation_formula': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, key=None, value_type=None, display_name=None, data_type_id=None, type=None, unit_schema=None, domain=None, scope=None, code=None, value_required=None, life_time=None, constraint_style=None, property_definition_type=None, property_description=None, derivation_formula=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PropertyDefinitionSearchResult - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param key:  The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.
        :type key: str
        :param value_type:  The type of values that can be associated with this property. This is defined by the property's data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel
        :type value_type: str
        :param display_name:  The display name of the property.
        :type display_name: str
        :param data_type_id: 
        :type data_type_id: lusid.ResourceId
        :param type:  The type of the property. The available values are: Label, Metric, Information
        :type type: str
        :param unit_schema:  The units that can be associated with the property's values. This is defined by the property's data type. The available values are: NoUnits, Basic, Iso4217Currency
        :type unit_schema: str
        :param domain:  The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity
        :type domain: str
        :param scope:  The scope that the property exists in.
        :type scope: str
        :param code:  The code of the property. Together with the domain and scope this uniquely identifies the property.
        :type code: str
        :param value_required:  This field is not implemented and should be disregarded.
        :type value_required: bool
        :param life_time:  Describes how the property's values can change over time. The available values are: Perpetual, TimeVariant
        :type life_time: str
        :param constraint_style:  Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key.
        :type constraint_style: str
        :param property_definition_type:  The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition
        :type property_definition_type: str
        :param property_description:  A brief description of what a property of this property definition contains.
        :type property_description: str
        :param derivation_formula:  The rule that defines how data is composed for a derived property.
        :type derivation_formula: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._key = None
        self._value_type = None
        self._display_name = None
        self._data_type_id = None
        self._type = None
        self._unit_schema = None
        self._domain = None
        self._scope = None
        self._code = None
        self._value_required = None
        self._life_time = None
        self._constraint_style = None
        self._property_definition_type = None
        self._property_description = None
        self._derivation_formula = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.key = key
        if value_type is not None:
            self.value_type = value_type
        self.display_name = display_name
        if data_type_id is not None:
            self.data_type_id = data_type_id
        if type is not None:
            self.type = type
        if unit_schema is not None:
            self.unit_schema = unit_schema
        if domain is not None:
            self.domain = domain
        self.scope = scope
        self.code = code
        if value_required is not None:
            self.value_required = value_required
        if life_time is not None:
            self.life_time = life_time
        self.constraint_style = constraint_style
        if property_definition_type is not None:
            self.property_definition_type = property_definition_type
        self.property_description = property_description
        self.derivation_formula = derivation_formula
        self.links = links

    @property
    def href(self):
        """Gets the href of this PropertyDefinitionSearchResult.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PropertyDefinitionSearchResult.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this PropertyDefinitionSearchResult.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def key(self):
        """Gets the key of this PropertyDefinitionSearchResult.  # noqa: E501

        The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.  # noqa: E501

        :return: The key of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PropertyDefinitionSearchResult.

        The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.  # noqa: E501

        :param key: The key of this PropertyDefinitionSearchResult.  # noqa: E501
        :type key: str
        """

        self._key = key

    @property
    def value_type(self):
        """Gets the value_type of this PropertyDefinitionSearchResult.  # noqa: E501

        The type of values that can be associated with this property. This is defined by the property's data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel  # noqa: E501

        :return: The value_type of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this PropertyDefinitionSearchResult.

        The type of values that can be associated with this property. This is defined by the property's data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel  # noqa: E501

        :param value_type: The value_type of this PropertyDefinitionSearchResult.  # noqa: E501
        :type value_type: str
        """
        allowed_values = ["String", "Int", "Decimal", "DateTime", "Boolean", "Map", "List", "PropertyArray", "Percentage", "Code", "Id", "Uri", "CurrencyAndAmount", "TradePrice", "Currency", "MetricValue", "ResourceId", "ResultValue", "CutLocalTime", "DateOrCutLabel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def display_name(self):
        """Gets the display_name of this PropertyDefinitionSearchResult.  # noqa: E501

        The display name of the property.  # noqa: E501

        :return: The display_name of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PropertyDefinitionSearchResult.

        The display name of the property.  # noqa: E501

        :param display_name: The display_name of this PropertyDefinitionSearchResult.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def data_type_id(self):
        """Gets the data_type_id of this PropertyDefinitionSearchResult.  # noqa: E501


        :return: The data_type_id of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._data_type_id

    @data_type_id.setter
    def data_type_id(self, data_type_id):
        """Sets the data_type_id of this PropertyDefinitionSearchResult.


        :param data_type_id: The data_type_id of this PropertyDefinitionSearchResult.  # noqa: E501
        :type data_type_id: lusid.ResourceId
        """

        self._data_type_id = data_type_id

    @property
    def type(self):
        """Gets the type of this PropertyDefinitionSearchResult.  # noqa: E501

        The type of the property. The available values are: Label, Metric, Information  # noqa: E501

        :return: The type of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertyDefinitionSearchResult.

        The type of the property. The available values are: Label, Metric, Information  # noqa: E501

        :param type: The type of this PropertyDefinitionSearchResult.  # noqa: E501
        :type type: str
        """
        allowed_values = ["Label", "Metric", "Information"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unit_schema(self):
        """Gets the unit_schema of this PropertyDefinitionSearchResult.  # noqa: E501

        The units that can be associated with the property's values. This is defined by the property's data type. The available values are: NoUnits, Basic, Iso4217Currency  # noqa: E501

        :return: The unit_schema of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._unit_schema

    @unit_schema.setter
    def unit_schema(self, unit_schema):
        """Sets the unit_schema of this PropertyDefinitionSearchResult.

        The units that can be associated with the property's values. This is defined by the property's data type. The available values are: NoUnits, Basic, Iso4217Currency  # noqa: E501

        :param unit_schema: The unit_schema of this PropertyDefinitionSearchResult.  # noqa: E501
        :type unit_schema: str
        """
        allowed_values = ["NoUnits", "Basic", "Iso4217Currency"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unit_schema not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unit_schema` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_schema, allowed_values)
            )

        self._unit_schema = unit_schema

    @property
    def domain(self):
        """Gets the domain of this PropertyDefinitionSearchResult.  # noqa: E501

        The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity  # noqa: E501

        :return: The domain of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PropertyDefinitionSearchResult.

        The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity  # noqa: E501

        :param domain: The domain of this PropertyDefinitionSearchResult.  # noqa: E501
        :type domain: str
        """
        allowed_values = ["NotDefined", "Transaction", "Portfolio", "Holding", "ReferenceHolding", "TransactionConfiguration", "Instrument", "CutLabelDefinition", "Analytic", "PortfolioGroup", "Person", "AccessMetadata", "Order", "UnitResult", "MarketData", "ConfigurationRecipe", "Allocation", "Calendar", "LegalEntity", "Placement", "Execution", "Block", "Participation", "Package", "OrderInstruction", "NextBestAction", "CustomEntity"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and domain not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `domain` ({0}), must be one of {1}"  # noqa: E501
                .format(domain, allowed_values)
            )

        self._domain = domain

    @property
    def scope(self):
        """Gets the scope of this PropertyDefinitionSearchResult.  # noqa: E501

        The scope that the property exists in.  # noqa: E501

        :return: The scope of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PropertyDefinitionSearchResult.

        The scope that the property exists in.  # noqa: E501

        :param scope: The scope of this PropertyDefinitionSearchResult.  # noqa: E501
        :type scope: str
        """

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this PropertyDefinitionSearchResult.  # noqa: E501

        The code of the property. Together with the domain and scope this uniquely identifies the property.  # noqa: E501

        :return: The code of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PropertyDefinitionSearchResult.

        The code of the property. Together with the domain and scope this uniquely identifies the property.  # noqa: E501

        :param code: The code of this PropertyDefinitionSearchResult.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def value_required(self):
        """Gets the value_required of this PropertyDefinitionSearchResult.  # noqa: E501

        This field is not implemented and should be disregarded.  # noqa: E501

        :return: The value_required of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: bool
        """
        return self._value_required

    @value_required.setter
    def value_required(self, value_required):
        """Sets the value_required of this PropertyDefinitionSearchResult.

        This field is not implemented and should be disregarded.  # noqa: E501

        :param value_required: The value_required of this PropertyDefinitionSearchResult.  # noqa: E501
        :type value_required: bool
        """

        self._value_required = value_required

    @property
    def life_time(self):
        """Gets the life_time of this PropertyDefinitionSearchResult.  # noqa: E501

        Describes how the property's values can change over time. The available values are: Perpetual, TimeVariant  # noqa: E501

        :return: The life_time of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._life_time

    @life_time.setter
    def life_time(self, life_time):
        """Sets the life_time of this PropertyDefinitionSearchResult.

        Describes how the property's values can change over time. The available values are: Perpetual, TimeVariant  # noqa: E501

        :param life_time: The life_time of this PropertyDefinitionSearchResult.  # noqa: E501
        :type life_time: str
        """
        allowed_values = ["Perpetual", "TimeVariant"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and life_time not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `life_time` ({0}), must be one of {1}"  # noqa: E501
                .format(life_time, allowed_values)
            )

        self._life_time = life_time

    @property
    def constraint_style(self):
        """Gets the constraint_style of this PropertyDefinitionSearchResult.  # noqa: E501

        Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key.  # noqa: E501

        :return: The constraint_style of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._constraint_style

    @constraint_style.setter
    def constraint_style(self, constraint_style):
        """Sets the constraint_style of this PropertyDefinitionSearchResult.

        Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key.  # noqa: E501

        :param constraint_style: The constraint_style of this PropertyDefinitionSearchResult.  # noqa: E501
        :type constraint_style: str
        """

        self._constraint_style = constraint_style

    @property
    def property_definition_type(self):
        """Gets the property_definition_type of this PropertyDefinitionSearchResult.  # noqa: E501

        The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition  # noqa: E501

        :return: The property_definition_type of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._property_definition_type

    @property_definition_type.setter
    def property_definition_type(self, property_definition_type):
        """Sets the property_definition_type of this PropertyDefinitionSearchResult.

        The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition  # noqa: E501

        :param property_definition_type: The property_definition_type of this PropertyDefinitionSearchResult.  # noqa: E501
        :type property_definition_type: str
        """
        allowed_values = ["ValueProperty", "DerivedDefinition"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and property_definition_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `property_definition_type` ({0}), must be one of {1}"  # noqa: E501
                .format(property_definition_type, allowed_values)
            )

        self._property_definition_type = property_definition_type

    @property
    def property_description(self):
        """Gets the property_description of this PropertyDefinitionSearchResult.  # noqa: E501

        A brief description of what a property of this property definition contains.  # noqa: E501

        :return: The property_description of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._property_description

    @property_description.setter
    def property_description(self, property_description):
        """Sets the property_description of this PropertyDefinitionSearchResult.

        A brief description of what a property of this property definition contains.  # noqa: E501

        :param property_description: The property_description of this PropertyDefinitionSearchResult.  # noqa: E501
        :type property_description: str
        """

        self._property_description = property_description

    @property
    def derivation_formula(self):
        """Gets the derivation_formula of this PropertyDefinitionSearchResult.  # noqa: E501

        The rule that defines how data is composed for a derived property.  # noqa: E501

        :return: The derivation_formula of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._derivation_formula

    @derivation_formula.setter
    def derivation_formula(self, derivation_formula):
        """Sets the derivation_formula of this PropertyDefinitionSearchResult.

        The rule that defines how data is composed for a derived property.  # noqa: E501

        :param derivation_formula: The derivation_formula of this PropertyDefinitionSearchResult.  # noqa: E501
        :type derivation_formula: str
        """

        self._derivation_formula = derivation_formula

    @property
    def links(self):
        """Gets the links of this PropertyDefinitionSearchResult.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PropertyDefinitionSearchResult.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PropertyDefinitionSearchResult.

        Collection of links.  # noqa: E501

        :param links: The links of this PropertyDefinitionSearchResult.  # noqa: E501
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
        if not isinstance(other, PropertyDefinitionSearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyDefinitionSearchResult):
            return True

        return self.to_dict() != other.to_dict()
