<template>
  <aside>
    <b-container>
      <b-card header="キーワードで検索" header-text-variant="light" header-bg-variant="dark" class="my-3">
        <SearchForm />
      </b-card>
      <b-card header="タグクラウド" header-text-variant="light" header-bg-variant="dark" class="my-3">
        #タグ1 #タグ2 #タグ3<br>
        #タグ4 #タグ5 #タグ6<br>
        #タグ7 #タグ8 #タグ9<br>
      </b-card>
      <b-card no-body header="カテゴリー" header-text-variant="light" header-bg-variant="dark" class="my-3">
        <CategoryList />
      </b-card>
      <b-card no-body header="人気記事" header-text-variant="light" header-bg-variant="dark" class="my-3">
        <PopularPostList />
      </b-card>
      <b-card no-body header="最新記事" header-text-variant="light" header-bg-variant="dark" class="my-3">
        <RecentPostList />
      </b-card>
      <b-card header="Twitter" header-text-variant="light" header-bg-variant="dark" class="my-3">
        Tweets
      </b-card>
    </b-container>
  </aside>
</template>

<script>
export default {
  name: "BlogSidebar",
};
</script>
