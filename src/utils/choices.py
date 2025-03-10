from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
    ('male', _('Male')),
    ('female', _('Female')),
    ('other', _('Other')),
    ('undisclosed', _('Undisclosed'))
)

UF_CHOICES = (
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MS', 'MS'),
    ('MT', 'MT'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
)

PROFILE_TYPE_CHOICES = (
    ('owner', _('Document Owner')),
    ('defult', _('Default')),
)

OPINION_VOTE_CHOICES = (
    ('approve', _('Approve')),
    ('reject', _('Reject')),
    ('neutral', _('Neutral')),
)

PARTICIPATION_GROUP_CHOICES = (
    ('waiting', _('Waiting')),
    ('in_progress', _('In Progress')),
)
