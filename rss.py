from core import plugin, model

class _rss(plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        model.registerModel("rss","_rss","_trigger","plugins.rss.models.trigger")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("rss","_rss","_trigger","plugins.rss.models.trigger")
        return True

    def upgrade(self,LatestPluginVersion):
        pass
    