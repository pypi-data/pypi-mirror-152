from anaml_client import Anaml
from anaml_client.models.ref import BranchRef
from anaml_client.models.table import RootTable, ViewTable, TableId, TableName
from anaml_client.models.feature import Feature, RowFeature, EventFeature, FeatureId, FeatureName, FeatureVersionId
from anaml_client.models.feature_set import FeatureSet, FeatureSetName, FeatureSetId, FeatureSetVersionId
from anaml_client.models.entity import Entity, EntityId, EntityName, EntityVersionId
from anaml_client.models.event_window import RowWindow, OpenWindow, DayWindow, EventWindow
from anaml_client.models.select_expression import SelectExpression
from anaml_client.models.filter_expression import FilterExpression
from anaml_client.models.source import SourceId, SourceName
from anaml_client.models.source_reference import SourceReference
from anaml_client.models.post_aggregate_expression import PostAggregateExpression
from anaml_client.models.aggregate import AggregateExpression
from anaml_client.models.schedule import DailySchedule, CronSchedule
from anaml_client.models.attribute import Attribute
from anaml_client.models.label import Label
from anaml_client.models.feature_store import FeatureStore, FeatureStoreId, FeatureStoreName
from anaml_client.models.feature_creation_request import FeatureCreationRequest, EventFeatureCreationRequest, RowFeatureCreationRequest
from anaml_client.models.table_creation_request import RootTableCreationRequest, ViewTableCreationRequest, TableCreationRequest, PivotTableCreationRequest
from anaml_client.models.entity_mapping import EntityMappingId, EntityMapping
from anaml_client.models.feature_set_creation_request import FeatureSetCreationRequest
import uuid
from uuid import UUID
import requests
from abc import ABC, abstractmethod
import os,io,json
from datetime import date, datetime, timezone, timedelta
from requests.auth import HTTPBasicAuth
from functools import partial
from dataclasses import dataclass, replace
from typing import Optional, List, Dict, Set, Callable

###Usage
#from anaml_client import Anaml
#from anaml_helper import AnamlHelper

#anaml_client = Anaml(url=,apikey=,secret=,ref=)
#anaml_helper = AnamlHelper(anaml_client)

###Aims 
#Provide access to lower level methods i.e update_feature_name() opposed to update_feature()
#Allows easier usage of sdk with features and feature sets
#as simplifies parameters by omitting the need to construct 
#complete Anaml objects to pass as parameter for updating certain attributes.

#Also aims to simplify feature creation process by
#providing method with params to create feature
#instead of expecting constructed EventFeatureCreationRequest to
#be passed to anaml.create_feature()

class AnamlHelper:
    """Helper class for working with Features and FeatureSets leveraging the existing Anaml Python SDK.
    
    ###Usage
    from anaml_client import Anaml
    from anaml_helper import AnamlHelper

    anaml_client = Anaml(url=,apikey=,secret=,ref=)
    anaml_helper = AnamlHelper(anaml_client)
    """
    __slots__ = ("_anaml")
    
    def __init__(self, anaml: Anaml) -> None:
        self._anaml = anaml

    @classmethod
    def from_client(cls, anaml: Anaml):
        return cls(anaml)
        
    @property
    def url(self) -> str:
        return self._anaml._url
    
    @property
    def branch(self) -> str:
        return self._anaml._ref.get("branch")
    
    #private method for handling aggregate type
    def __get_aggregate_type(self, aggregate: str) -> AggregateExpression:
        aggregations = {
            "count": AggregateExpression.Count,
            "countdistinct": AggregateExpression.CountDistinct,
            "last": AggregateExpression.Last,
            "first": AggregateExpression.First,
            "max": AggregateExpression.Max,
            "min": AggregateExpression.Min,
            "sum": AggregateExpression.Sum,
            "avg": AggregateExpression.Avg
        }
        return aggregations.get(aggregate.lower())

    #private method for generating new commit id
    def __generate_commit_id(self) -> UUID:
        return uuid.uuid4()
    
    ###Creating Features
    def create_feature(self,
                       name: str,
                       attributes: List[dict[str,str]],
                       labels: List[str],
                       select: str,
                       description: str,
                       template: Optional[str],
                       table: int,
                       filter: str,
                       aggregate: str,
                       post_aggregate: str,
                       entity_ids: List[int]
                       ) -> EventFeature:
        creation_request = EventFeatureCreationRequest(
            attributes=[Attribute.from_json(attr) for attr in attributes],
            labels=[Label(label) for label in labels],
            name=FeatureName(value=name),
            description=description,
            select=SelectExpression(sql=select),
            template=template,
            table=TableId(value=table),
            window=OpenWindow(),
            filter=FilterExpression(sql=filter),
            aggregate=self.__get_aggregate_type(aggregate),
            postAggregateExpr=PostAggregateExpression(sql=post_aggregate),
            entityRestrictions=[EntityId(entity) for entity in entity_ids]
        )
        return self._anaml.create_feature(creation_request)

    ###Updating Features
    def update_feature_name(self, feature_id: int, name: str) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, name=FeatureName(name), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_attributes(self, feature_id: int, attributes: Dict[str,str]) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        new_attributes = [Attribute(key=k, value=v) for k,v in attributes.items()]
        updated_feature = replace(current_feature, attributes=new_attributes, version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_description(self, feature_id: int, description: str) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, description=description, version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_labels(self, feature_id: int, labels: List[str]) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        new_labels = [Label(value=label) for label in labels]
        updated_feature = replace(current_feature, labels=new_labels, version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_table(self, feature_id: int, table_id: int) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, table=TableId(value=table_id), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_select(self, feature_id: int, select_expression: str) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, select=SelectExpression(sql=select_expression), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_filter(self, feature_id: int, filter_expression: str) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, filter=FilterExpression(sql=filter_expression), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_aggregate(self, feature_id: int, aggregate: str) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, aggregate=self.__get_aggregate_type(aggregate), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_to_RowWindow(self, feature_id: int, rows: int) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, window=RowWindow(rows=rows), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_to_DayWindow(self, feature_id: int, days: int) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, window=DayWindow(days=days), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_to_OpenWindow(self, feature_id: int) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, window=OpenWindow(), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
    
    def update_feature_postAggregateExpr(self, feature_id: int, post_agg_expression: str) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, postAggregateExpr=PostAggregateExpression(sql=post_agg_expression), version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_entityRestrictions(self, feature_id: int, entity_ids: List[int]) -> EventFeature:
        current_feature = self._anaml.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, entityRestrictions=[EntityId(entity) for entity in entity_ids], version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    def update_feature_template(self, feature_id: int, template: str) -> EventFeature:
        current_feature = self._anam.get_feature_by_id(feature_id)
        updated_feature = replace(current_feature, template=template, version=FeatureVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature(updated_feature)
        
    ###Creating Feature Sets
    def create_featureset(self,
                          name: str,
                          entity: int,
                          description: str,
                          labels: List[str],
                          attributes: List[dict[str,str]],
                          features: List[int]):
        creation_request = FeatureSetCreationRequest(
                    name=FeatureSetName(value=name),
                    entity=EntityId(entity),
                    description=description,
                    labels=[Label(label) for label in labels],
                    attributes=[Attribute.from_json(attr) for attr in attributes],
                    features=[FeatureId(feature_id) for feature_id in features]
        )
        return self._anaml.create_feature_set(creation_request)
    
    ###Updating Feature Sets
    def update_featureset_name(self, featureset_id: int, name: str) -> FeatureSet:
        current_featureset = self._anaml.get_feature_set_by_id(featureset_id)
        updated_featureset = replace(current_featureset, name=FeatureSetName(value=name), version=FeatureSetVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature_set(updated_featureset)
        
    def update_featureset_entity(self, featureset_id: int, entity_id: int) -> FeatureSet:
        current_featureset = self._anaml.get_feature_set_by_id(featureset_id)
        updated_featureset = replace(current_featureset, entity=EntityId(value=entity_id), version=FeatureSetVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature_set(updated_feature)
        
    def update_featureset_description(self, featureset_id: int, description: str) -> FeatureSet:
        current_featureset = self._anaml.get_feature_set_by_id(featureset_id)
        updated_featureset = replace(current_featureset, description=description, version=FeatureSetVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature_set(updated_featureset)
        
    def update_featureset_labels(self, featureset_id: int, labels: List[str]) -> FeatureSet:
        current_featureset = self._anaml.get_feature_set_by_id(featureset_id)
        new_labels = [Label(label) for label in labels]
        updated_featureset = replace(current_featureset, labels=new_labels, version=FeatureSetVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature_set(updated_featureset)
    
    def update_featureset_attributes(self, featureset_id: int, attributes: dict[str,str]) -> FeatureSet:
        current_featureset = self._anaml.get_feature_set_by_id(featureset_id)
        new_attributes = [Attribute(key=k,value=v) for k,v in attributes.items()]
        updated_featureset = replace(current_featureset, attributes=new_attributes, version=FeatureSetVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature_set(updated_featureset)
        
    def update_featureset_features(self, featureset_id: int, features: List[int]) -> FeatureSet:
        current_featureset = self._anaml.get_feature_set_by_id(featureset_id)
        new_features = [FeatureId(value=feature_id) for feature_id in features]
        updated_featureset = replace(current_featureset, labels=new_labels, version=FeatureSetVersionId(self.__generate_commit_id()))
        return self._anaml.update_feature_set(updated_featureset)

    ##Creating tables
    def create_root_table(self,
                        attributes: Dict[str,str],
                        description: Optional[str],
                        labels: List[str],
                        name: str,
                        entity_mappings: Dict[int,str],
                        timestamp_col: str,
                        source: int):
        return self._anaml.create_table(
                RootTableCreationRequest(
                    attributes=[Attribute(key=k,value=v) for k,v in attributes.items()],
                    description=description,
                    labels=[Label(value=label) for label in labels],
                    name=TableName(value=name),
                    eventDescription=EventDescription(
                        entities=entity_mappings,
                        timestampInfo=timestamp_col
                    ),
                    source=SourceReference(SourceId(source))
                ))

    def create_view_table(self,
                        attributes: Dict[str,str],
                        description: Optional[str],
                        labels: List[str],
                        name: str,
                        entity_mappings: Dict[int,str],
                        timestamp_col: str,
                        expression: str,
                        sources: List[int]):
        return self._anaml.create_table(ViewTableCreationRequest(
                        attributes=[Attribute(key=k,value=v) for k,v in attributes.items()],
                        description=description,
                        labels=[Label(value=label) for label in labels],
                        name=TableName(value=name),
                        eventDescription=EventDescription(
                            entities=entity_mappings,
                            timestampInfo=timestamp_col,
                        ),
                        expression=expression,
                        sources=[TableId(value=table_id) for table_id in table_ids]))

    def create_pivot_table(self,
                        attributes: List[str],
                        description: Optional[str],
                        labels: List[str],
                        name: str,
                        entity_mapping: int,
                        extra_features: List[int]):
        return self._anaml.create_table(PivotTableCreationRequest(
            attributes=[Attribute(key=k,value=v) for k,v in attributes.items()],
            description=description,
            labels=[Label(value=label) for label in labels],
            name=TableName(value=name),
            entityMapping=EntityMappingId(value=entity_mapping),
            extraFeatures=[FeatureId(value=feature_id) for feature_id in extra_features]))

    #Updating tables
    def update_table_name(self,
                        table_id: int,
                        name: str):
        return self._anaml.update_table(
            replace(self._anaml.get_table_by_id(table_id),
                    name=name,
                    version=FeatureVersionId(self.__generate_commit_id())))
        
    def update_table_description(self,
                                table_id: int,
                                description: str):
        return self._anaml.update_table(
            replace(self._anaml.get_table_by_id(table_id),
                    description=description,
                    version=FeatureVersionId(self.__generate_commit_id())))
        
    def update_table_labels(self,
                            table_id: int,
                            labels: List[str]):
        return self._anaml.update_table(
            replace(self._anaml.get_table_by_id(table_id),
                    labels=[Label(label) for label in labels],
                    version=FeatureVersionId(self.__generate_commit_id())))
    def update_table_attributes(self,
                                table_id: int,
                                attributes: Dict[str,str]):
        return self._anaml.update_table(
            replace(self._anaml.get_table_by_id(table_id),
                    attributes=[Attribute(key=k,value=v) for k,v in attributes.items()],
                    version=FeatureVersionId(self.__generate_commit_id())))

    def update_root_table_source(self,
                                root_table_id: int,
                                source_id: int):
        return self._anaml.update_table(
            replace(self._anaml.get_table_by_id(table_id),
                    source=SourceId(source_id),
                    version=FeatureVersionId(self.__generate_commit_id())))

    def update_view_table_sources(self,
                                view_table_id: int,
                                sources: List[int]):
        return self._anaml.update_table(replace(self._anaml.get_table_by_id(table_id), 
                                sources=[SourceId(source) for source in sources],
                                version=FeatureVersionId(self.__generate_commit_id())))
        
    def update_view_table_expression(self,
                                    view_table_id: int,
                                    expression: str):
        return self._anaml.update_table(replace(self._anaml.get_table_by_id(table_id),
                                expression=expression,
                                version=FeatureVersionId(self.__generate_commit_id())))