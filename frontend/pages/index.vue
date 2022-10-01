<template>
  <div>
    <b-jumbotron header="Title" lead="Subtitle" fluid>
      <p>Text</p>
      <b-button variant="dark"  :to="{name: 'signup'}">参加する</b-button>
    </b-jumbotron>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>
