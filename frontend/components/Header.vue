<template>
  <header>
    <div class="mb-5">
      <b-navbar toggleable="lg">
        <b-container>
          <b-navbar-brand :to="{name: 'index'}">Title</b-navbar-brand>
          <b-navbar-toggle target="nav-text-collapse"></b-navbar-toggle>
          <b-collapse id="nav-text-collapse" is-nav>
            <b-navbar-nav>
              <b-nav-item :to="{name: 'blog'}">Blog</b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class="ml-auto">
              <b-nav-item :to="{name: 'signin'}">ログイン</b-nav-item>
              <b-nav-item :to="{name: 'signup'}">登録</b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-container>
      </b-navbar>
    </div>
  </header>
</template>

<script>
export default {
  name: "PageHeader",
};
</script>
