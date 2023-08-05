from typing import List, Optional, Union

from pydantic import BaseModel

from watchmen_model.common import construct_parameter, construct_parameter_joint, FactorId, Parameter
from watchmen_utilities import ArrayHelper
from .pipeline_action import AggregateArithmeticHolder, FindBy, PipelineAction, ToFactor, ToTopic, WriteTopicActionType


class MappingFactor(AggregateArithmeticHolder, BaseModel):
	source: Parameter = None
	factorId: FactorId = None

	def __setattr__(self, name, value):
		if name == 'source':
			super().__setattr__(name, construct_parameter(value))
		else:
			super().__setattr__(name, value)


class MappingRow(PipelineAction):
	mapping: List[MappingFactor] = []


class WriteTopicAction(ToTopic):
	type: WriteTopicActionType = None


def construct_mapping_factor(condition: Optional[Union[dict, MappingFactor]]) -> Optional[MappingFactor]:
	if condition is None:
		return None
	elif isinstance(condition, MappingFactor):
		return condition
	else:
		return MappingFactor(**condition)


def construct_mapping(conditions: Optional[list]) -> Optional[List[MappingFactor]]:
	if conditions is None:
		return None
	return ArrayHelper(conditions).map(lambda x: construct_mapping_factor(x)).to_list()


class InsertRowAction(WriteTopicAction, MappingRow):
	type: WriteTopicActionType = WriteTopicActionType.INSERT_ROW

	def __setattr__(self, name, value):
		if name == 'mapping':
			super().__setattr__(name, construct_mapping(value))
		else:
			super().__setattr__(name, value)


class InsertOrMergeRowAction(WriteTopicAction, MappingRow, FindBy):
	type: WriteTopicActionType = WriteTopicActionType.INSERT_OR_MERGE_ROW

	def __setattr__(self, name, value):
		if name == 'mapping':
			super().__setattr__(name, construct_mapping(value))
		elif name == 'by':
			super().__setattr__(name, construct_parameter_joint(value))
		else:
			super().__setattr__(name, value)


class MergeRowAction(WriteTopicAction, MappingRow, FindBy):
	type: WriteTopicActionType = WriteTopicActionType.MERGE_ROW

	def __setattr__(self, name, value):
		if name == 'mapping':
			super().__setattr__(name, construct_mapping(value))
		elif name == 'by':
			super().__setattr__(name, construct_parameter_joint(value))
		else:
			super().__setattr__(name, value)


class WriteFactorAction(ToFactor, WriteTopicAction, FindBy, AggregateArithmeticHolder):
	type: WriteTopicActionType = WriteTopicActionType.WRITE_FACTOR
	source: Parameter = None

	def __setattr__(self, name, value):
		if name == 'mapping':
			super().__setattr__(name, construct_mapping(value))
		elif name == 'by':
			super().__setattr__(name, construct_parameter_joint(value))
		elif name == 'source':
			super().__setattr__(name, construct_parameter(value))
		else:
			super().__setattr__(name, value)
