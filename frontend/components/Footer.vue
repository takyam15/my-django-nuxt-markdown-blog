<template>
  <footer>
    <div class="text-center mt-5">
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-toggle target="nav-text-collapse"></b-navbar-toggle>
        <b-collapse id="nav-text-collapse" is-nav>
          <b-navbar-nav class="mx-auto">
            <b-nav-item :to="{name: 'terms'}">利用規約</b-nav-item>
            <b-nav-item :to="{name: 'privacy'}">プライバシーポリシー</b-nav-item>
            <b-nav-item :to="{name: 'contact'}">お問い合わせ</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
      <small class="text-dark">©2022 Title</small>
    </div>
  </footer>
</template>

<script>
export default {
  name: "PageFooter",
};
</script>
