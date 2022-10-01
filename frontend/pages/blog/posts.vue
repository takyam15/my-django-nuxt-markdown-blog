<template>
  <b-row>
    <b-col md="9">
      <b-container>
        <h1 class="text-center font-weight-bold">ブログ記事一覧</h1>
        <div v-for="post in posts" :key="post.slug" class="my-3">
          <b-card class="overflow-hidden">
            <b-row no-gutters>
              <b-col md="3">
                <b-card-img src="https://picsum.photos/400/400/?image=20" alt="Image" class="rounded-0"></b-card-img>
              </b-col>
              <b-col md="9">
                <b-container>
                  <b-card-text text-tag="h2" class="font-weight-bold">
                    <b-link :to="{name: 'blog-slug', params: {slug: post.slug}}" class="card-link text-dark">{{ post.title }}</b-link>
                  </b-card-text>
                  <div class="my-3">
                    <b-button size="sm" squared>{{ post.category }}</b-button>
                  </div>
                  <div class="my-3">
                    <b-list-group horizontal="md">
                      <b-list-group-item v-for="tag in post.tags" :key="tag.slug"><b-link :to="{name: 'blog-posts'}" class="card-link">{{ tag }}</b-link></b-list-group-item>
                    </b-list-group>
                  </div>
                  <b-card-text>{{ post.description }}</b-card-text>
                </b-container>
              </b-col>
            </b-row>
          </b-card>
        </div>
      </b-container>
    </b-col>
    <b-col md="3">
      <BlogSidebar />
    </b-col>
  </b-row>
</template>

<script>
const axios = require('axios');
const url = '/api/blog/posts';
export default {
  name: 'BlogPosts',
  asyncData({ params }) {
    return axios.get(url)
    .then ((res => {
      return {
        posts: res.data
      }
    }))
    .catch ((e => {
      return {
        statusCode: e.status,
        message: e.message
      }
    }))
  },
  data () {
    return {
      posts: []
    }
  },
}
</script>
