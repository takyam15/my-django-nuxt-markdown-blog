<template>
  <b-row>
    <b-col md="3">
      <BlogTOC />
    </b-col>
    <b-col md="6">
      <b-container>
        <h1 class="text-center font-weight-bold">{{ post.title }}</h1>
        <div class="my-3">
          <b-button size="sm" squared>{{ post.category }}</b-button>
        </div>
        <div class="my-3">
          <b-list-group horizontal="md">
            <b-list-group-item>最終更新日: {{ post.updated_at }}</b-list-group-item>
            <b-list-group-item>公開日: {{ post.published_at }}</b-list-group-item>
          </b-list-group>
        </div>
        <div v-html="post.body" class="markdown-x"></div>
        <div class="my-5">
          <b-list-group horizontal="md">
            <b-list-group-item v-for="tag in post.tags" :key="tag.slug"><b-link :to="{name: 'blog-posts'}" class="card-link">{{ tag }}</b-link></b-list-group-item>
          </b-list-group>
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
export default {
  name: 'BlogSlug',
  asyncData({ params }) {
    const url = '/api/blog/posts/' + params.slug;
    return axios.get(url)
    .then ((res => {
      return {
        post: res.data
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
      post: []
    }
  },
}
</script>

<style>
.markdown-x h2 {
  border-bottom: 1px solid #ddd;
}
.markdown-x h2, .markdown-x h3, .markdown-x h4, .markdown-x h5, .markdown-x h6 {
  font-weight: bold;
  line-height: 1.5;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
