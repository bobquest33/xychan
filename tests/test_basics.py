
from bottle import debug
from paste.fixture import TestApp

from xychan import app
from xychan.db import configure_db, Post, Thread, Board, active_session

debug(True)
configure_db('sqlite:///:memory:', echo=False)

app = TestApp(app)

def setUp():
    with active_session:
        s.query(Post).delete()
        s.query(Thread).delete()
        s.query(Board).delete()
    app.get('/setup')


def test_home():
    r = app.get('/')


def test_post_to_board():
    r = app.post('/test/post', params=dict(
            content="Test post 2242"))
    r = app.get('/test/')
    assert "Test post 2242" in r


def test_visit_board():
    r = app.get('/test/')
    assert "This is a post" in r
    r = app.get('/test')
    assert "This is a post" in r


def test_visit_thread():
    r = app.get('/test/1/')
    assert "This is a post" in r
    r = app.get('/test/1')
    assert "This is a post" in r


def test_thread_order():
    r = app.post('/test/post', params=dict(
            content="Test post NEW"))
    r = app.get('/test')
    assert r.body.index("Test post NEW") < r.body.index("This is a post")


def test_post_list():
    app.post('/test/post', params=dict(
            content="Test post OP"))
    for x in range(10):
        app.post('/test/1/post', params=dict(
                content="Test post #" + str(x)))
    r = app.get('/test')
    assert "Test post OP" in r
    assert "Test post #3" not in r
    assert "Test post #9" in r

