<template>
  <aside>
    <b-container>
      <b-card header="キーワードで検索" header-text-variant="light" header-bg-variant="success" class="mb-3 font-weight-bold">
        <SearchForm />
      </b-card>
      <b-card header="タグクラウド" header-text-variant="light" header-bg-variant="success" class="my-3 font-weight-bold">
        #タグ1 #タグ2 #タグ3<br>
        #タグ4 #タグ5 #タグ6<br>
        #タグ7 #タグ8 #タグ9<br>
      </b-card>
      <b-card no-body header="カテゴリー" header-text-variant="light" header-bg-variant="success" class="my-3 font-weight-bold">
        <CategoryList />
      </b-card>
      <b-card no-body header="人気記事" header-text-variant="light" header-bg-variant="success" class="my-3 font-weight-bold">
        <PopularPostList />
      </b-card>
      <b-card no-body header="最新記事" header-text-variant="light" header-bg-variant="success" class="my-3 font-weight-bold">
        <RecentPostList />
      </b-card>
      <b-card header="Twitter" header-text-variant="light" header-bg-variant="success" class="my-3 font-weight-bold">
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
