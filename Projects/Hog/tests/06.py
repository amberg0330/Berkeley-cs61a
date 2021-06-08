test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '5e0e1a4c94a7429afae6399105d34f05',
          'choices': [
            'Another commentary function.',
            'An integer representing the score.',
            'None.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does a commentary function return?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)
          d7882c94106188a2f424c5383b507923
          b706c6a1e63c19ed82e4eb95fc6ba1cf
          519a2e7c2e74bf29cb97b470402b22a2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def count(n):
          ...     def say(s0, s1):
          ...         print(n, s0)
          ...         return count(n + 1)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=10, say=count(1))
          61f188e55077f84722da3594df10f844
          072a7e5a36da4da6069d77fa89868297
          92aad6b5ebfdcdc3f09c28a51c2b7374
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          4 0 
          4 12 
          16 12 
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play.
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
          2 0 
          7 
          4 5 
          14 
          9 7 ##pig pass# 
          21 
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=3, say=both(echo_0, echo_1))
          * 2 
          ** 0 
          * 2 
          ** 2 
          * 4 
          ** 2
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes()))
          Player 0 now has 1 and Player 1 now has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and Player 1 now has 1
          Player 0 now has 2 and Player 1 now has 1
          Player 0 takes the lead by 1
          Player 0 now has 2 and Player 1 now has 9
          Player 1 takes the lead by 7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
