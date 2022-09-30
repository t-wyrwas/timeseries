from nox import session, Session

@session
def test(session: Session):
    session.run('pip', 'install', '-r', 'requirements.txt')
    session.run('pip', 'install', '-r', 'requirements-dev.txt')
    session.run('pytest', 'src', env={'PYTHONPATH': 'src'})
