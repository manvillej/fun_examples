from error_app import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    return "not found", 404


@bp.app_errorhandler(500)
def internal_error(error):
    return "internal error", 500