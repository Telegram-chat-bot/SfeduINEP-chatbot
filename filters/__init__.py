from .BackButton import CommandBack
from .ChatTypeFilter import IsGroup
from .MessageFilter import IsNotButton, OtherWords
from loader import dp

if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(CommandBack)
    dp.filters_factory.bind(IsNotButton)
    dp.filters_factory.bind(OtherWords)
