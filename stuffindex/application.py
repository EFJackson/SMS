from stuffindex import utils

conf = {}
conf['webapp2_extras.sessions'] = {'secret_key':
    """J-zAe5#S7qa<F'N[Xl])QEQq9ZKd6~ptGv0,Q&cDs<*5$FPgyWqfC*+MnOV>~8B*"""}

application = utils.WSGIApplication([], config=conf)
