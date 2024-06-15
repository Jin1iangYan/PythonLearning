def standard_arg(arg):
    print(arg)

standard_arg(2)        # 通过位置传递
standard_arg(arg=2)    # 通过关键字传递
print('-' * 40)


def pos_only_arg(arg, /):
    """
    def f(pos1, /):
      -----------
        |        
        |        
        |        
         -- Positional only
    """
    print(arg)

pos_only_arg(1)        # 通过位置传递
# pos_only_arg(arg=1)  # 通过关键字传递会报错
print('-' * 40)


def kwd_only_arg(*, arg):
    """
    def f(*, arg):
         ---------------
              |
              |
              - Keyword only
    """
    print(arg)

# kwd_only_arg(3)     # 通过位置传递会报错
kwd_only_arg(arg=3)    # 通过关键字传递
print('-' * 40)

def combined_example(pos_only, /, standard, *, kwd_only):
    """
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
    """
    print(pos_only, standard, kwd_only)

combined_example(1, 2, kwd_only=3)               # 正确
# combined_example(pos_only=1, standard=2, kwd_only=3)  # 仅限位置参数通过关键字传递会报错
print('-' * 40)
