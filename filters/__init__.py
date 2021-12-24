from .backButton import CommandBack
from .ChatTypeFilter import IsGroup
from loader import dp

if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(CommandBack)
