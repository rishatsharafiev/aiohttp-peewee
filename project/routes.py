from project.apps.bot.apps import bot_app


def setup_routes(app):
    """Setup application routes"""
    app.add_subapp('/bot/', bot_app)
