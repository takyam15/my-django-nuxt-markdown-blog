<template>
  <div>
    <h1 class="text-center my-5 font-weight-bold">ログイン</h1>

    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-row class="justify-content-md-center">
        <b-col md="4">

          <b-form-group id="input-group-username" label="ユーザー名" label-for="input-username">
            <b-form-input id="input-username" v-model="form.username" placeholder="ユーザー名" required></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-password" label="パスワード" label-for="input-password">
            <b-form-input id="input-password" v-model="form.password" type="password" placeholder="パスワード" required></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-agree" v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group v-model="form.checked" id="checkboxes-agree" :aria-describedby="ariaDescribedby">
              <b-form-checkbox>ログインしたままにする</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="dark">ログイン</b-button>

        </b-col>
      </b-form-row>

    </b-form>
      
  </div>
</template>

<script>
export default {
  name: 'SighIn',
  data() {
    return {
      form: {
        username: '',
        password: '',
        checked: []
      },
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset(event) {
      event.preventDefault()
      this.form.username = ''
      this.form.password = ''
      this.form.checked = []
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>
