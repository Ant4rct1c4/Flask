import unittest

from app import create_app, db
from app.posts.models import Post


class PostCRUDTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')

        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_post(self):
        response = self.client.post(
            '/post/create',
            data={
                'title': 'Test Post',
                'content': 'This is test content',
                'category': 'tech',
                'is_active': 'y',
                'publish_date': '2026-05-29T12:00'
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post added successfully', response.data)

        post = db.session.scalar(
            db.select(Post).where(Post.title == 'Test Post')
        )

        self.assertIsNotNone(post)

    def test_all_posts_page(self):
        post = Post(
            title='Visible Post',
            content='Some content',
            category='news',
            is_active=True
        )

        db.session.add(post)
        db.session.commit()

        response = self.client.get('/post/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visible Post', response.data)

    def test_detail_post_page(self):
        post = Post(
            title='Detail Post',
            content='Full post content',
            category='publication',
            is_active=True
        )

        db.session.add(post)
        db.session.commit()

        response = self.client.get(f'/post/{post.id}')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Detail Post', response.data)
        self.assertIn(b'Full post content', response.data)

    def test_update_post(self):
        post = Post(
            title='Old Title',
            content='Old content',
            category='other',
            is_active=True
        )

        db.session.add(post)
        db.session.commit()

        response = self.client.post(
            f'/post/{post.id}/update',
            data={
                'title': 'New Title',
                'content': 'New updated content',
                'category': 'tech',
                'is_active': 'y',
                'publish_date': '2026-05-29T13:00'
            },
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post updated successfully', response.data)

        updated_post = db.session.get(Post, post.id)

        self.assertEqual(updated_post.title, 'New Title')

    def test_delete_post(self):
        post = Post(
            title='Delete Me',
            content='Delete content',
            category='news',
            is_active=True
        )

        db.session.add(post)
        db.session.commit()

        post_id = post.id

        response = self.client.post(
            f'/post/{post_id}/delete',
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post deleted successfully', response.data)

        deleted_post = db.session.get(Post, post_id)

        self.assertIsNone(deleted_post)


if __name__ == '__main__':
    unittest.main()