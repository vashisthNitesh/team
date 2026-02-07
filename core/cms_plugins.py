from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import TeamMemberDetailPlugin, TeamMemberListPlugin


@plugin_pool.register_plugin
class TeamMemberListPluginCMSPlugin(CMSPluginBase):
    model = TeamMemberListPlugin
    name = _('Team Member List Card')
    module = _('Content')
    render_template = 'core/plugins/team_member_list_card.html'
    cache = False
    icon = 'cms-icon cms-icon-plugins'


@plugin_pool.register_plugin
class TeamMemberDetailPluginCMSPlugin(CMSPluginBase):
    model = TeamMemberDetailPlugin
    name = _('Team Member Detail Section')
    module = _('Content')
    render_template = 'core/plugins/team_member_detail_section.html'
    cache = False
    icon = 'cms-icon cms-icon-plugins'
