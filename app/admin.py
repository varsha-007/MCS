from django.contrib import admin
from django.db import models

from .models import *


def register_models(*models_to_register):
    for model in models_to_register:
        fields = [
            field.name
            for field in model._meta.get_fields()
            if isinstance(field, models.Field) and field.name != "id"
        ]
        admin.site.register(model, list_display=fields)


# Register your models using the function
register_models(
    ForwardPhysicalTextCard,
    PremOrDiscTable,
    ProxyBlendTable,
    OtherProductValuesTable,
    PrimaryvsSecondaryDifferentialTable,
    OnshoreValues,
    MysteelTable,
    FuturesTable,
    FuturesSubTable,
    SecondaryOffer,
    PortSideIron,
    PortSideIronTextCard1,
    PortSideIronTextCard2,
)
