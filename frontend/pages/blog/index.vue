<template>
  <b-container>
    <h1 class="text-center font-weight-bold">ブログ</h1>
    <h2 class="text-center font-weight-bold my-5">最初に読みたい記事</h2>
    <div>
      <b-card-group>
        <b-card img-src="https://picsum.photos/400/400/?image=20" img-alt="Image" img-top>
          <b-card-text text-tag="h3" class="font-weight-bold">記事タイトル</b-card-text>
          <div class="my-3">
            <b-button :to="{name: 'blog-posts'}" size="sm" squared>カテゴリー１</b-button>
          </div>
          <b-card-text>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。<br>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。<br>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。
          </b-card-text>
        </b-card>
        <b-card img-src="https://picsum.photos/400/400/?image=20" img-alt="Image" img-top>
          <b-card-text text-tag="h3" class="font-weight-bold">記事タイトル</b-card-text>
          <div class="my-3">
            <b-button :to="{name: 'blog-posts'}" size="sm" squared>カテゴリー２</b-button>
          </div>
          <b-card-text>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。<br>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。<br>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。
          </b-card-text>
        </b-card>
        <b-card img-src="https://picsum.photos/400/400/?image=20" img-alt="Image" img-top>
          <b-card-text text-tag="h3" class="font-weight-bold">記事タイトル</b-card-text>
          <div class="my-3">
            <b-button :to="{name: 'blog-posts'}" size="sm" squared>カテゴリー３</b-button>
          </div>
          <b-card-text>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。<br>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。<br>
            ブログのサンプル記事の概要文です。ブログのサンプル記事の概要文です。
          </b-card-text>
        </b-card>
      </b-card-group>
    </div>
  </b-container>
</template>

<script>
export default {
  name: 'BlogIndex',
}
</script>
