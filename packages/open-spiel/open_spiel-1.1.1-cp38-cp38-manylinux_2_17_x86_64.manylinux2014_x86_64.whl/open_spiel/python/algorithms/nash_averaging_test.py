# Copyright 2022 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for open_spiel.python.algorithms.nash_averaging."""

from absl.testing import absltest
from absl.testing import parameterized
import numpy as np

from open_spiel.python.algorithms.nash_averaging import nash_averaging
import pyspiel

# transitive game test case
game_trans = pyspiel.create_matrix_game(
    [[0.0, -1.0, -1.0], [1.0, 0.0, -1.0], [1.0, 1.0, 0.0]],
    [[0.0, 1.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, -1.0, 0.0]])

eq_trans = np.asarray([0., 0., 1.])
value_trans = np.asarray([-1., -1., 0.])

# rock-paper-scissors test case
game_rps = pyspiel.create_matrix_game(
    [[0.0, -1.0, 1.0], [1.0, 0.0, -1.0], [-1.0, 1.0, 0.0]],
    [[0.0, 1.0, -1.0], [-1.0, 0.0, 1.0], [1.0, -1.0, 0.0]])
eq_rps = np.asarray([1 / 3, 1 / 3, 1 / 3])
value_rps = np.asarray([0., 0., 0.])


class NashAveragingTest(parameterized.TestCase):

  @parameterized.named_parameters(
      ("transitive_game", game_trans, eq_trans, value_trans),
      ("rps_game", game_rps, eq_rps, value_rps),
  )
  def test_simple_games(self, game, eq, value):

    maxent_nash, nash_avg_value = nash_averaging(game)
    with self.subTest("probability"):
      np.testing.assert_array_almost_equal(eq, maxent_nash.reshape(-1))

    with self.subTest("value"):
      np.testing.assert_array_almost_equal(value, nash_avg_value.reshape(-1))


if __name__ == "__main__":
  absltest.main()
