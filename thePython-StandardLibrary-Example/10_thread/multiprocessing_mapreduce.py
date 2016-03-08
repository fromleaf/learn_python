# -*- coding:utf-8 -*-

import collections
import itertools
import multiprocessing

class SimpleMapReduce(object):
	def __init__(self, map_func, reduce_func, num_workers=None):
		"""
		map_func: 입력 값을 중간 데이터에 매핑하는 함수. 인자를 하나의 입력으로 받아
		리듀스할 키와 값을 튜플로 반환한다.
		
		reduce_func: 구분된 중간 데이터를 최종 결과로 리듀스하기 위한 함수.
		map_func에서 생성한 키와 이에 대응하는 연속된 값을 인자로 받는다.

		num_workers: 풀에서 생성할 워커의 개수.
		기본 값은 현재 호스트에서 사용할 수 있는 CPU의 수로 설정된다.
		"""
		
		self.map_func = map_func
		self.reduce_func = reduce_func
		self.pool = multiprocessing.Pool(num_workers)

	def partition(self, mapped_values):
		"""
		Arrange the values that have been mapped through keys.
		Keys and continoutly values are returned not arranged tuples type.
		"""
		
		partitioned_data = collections.defaultdict(list)
		for key, value in mapped_values:
			partitioned_data[key].append(value)
		return partitioned_data.items()

	def __call__(self, inputs, chunksize=1):
		"""
		To execute input values by map and reduce function

		inputs: recycleable input data

		chunksize=1: the part of input data that pass to each workers
		It can use for controlling performance during mapping.
		"""
		
		map_responses = self.pool.map(self.map_func,
									inputs,
									chunksize=chunksize)
		partitioned_data = self.partition(itertools.chain(*map_responses))
		reduced_values = self.pool.map(self.reduce_func,
									partitioned_data)
		return reduced_values

