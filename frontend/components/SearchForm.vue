<template>
  <b-form inline>
    <label class="sr-only" for="inline-form-input-name">Keyword</label>
    <b-form-input
    id="inline-form-input-name"
    class="mb-2 mr-sm-2 mb-sm-0"
    placeholder="キーワードを入力"
    ></b-form-input>
    <b-button variant="dark">検索</b-button>
  </b-form>
</template>

<script>
export default {
  name: "SearchForm",
};
</script>
