from pytest_factoryboy import register

import todolist.tests.factories as tests

register(tests.factories.UserFactory)
register(tests.factories.BoardFactory)
register(tests.factories.BoardParticipantFactory)
register(tests.factories.GoalCategoryFactory)
register(tests.factories.GoalCommentFactory)
register(tests.factories.GoalFactory)

pytest_plugins = 'tests.fixtures'
