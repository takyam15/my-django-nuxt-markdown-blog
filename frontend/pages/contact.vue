<template>
  <div>
    <h1 class="text-center my-5 font-weight-bold">お問い合わせ</h1>

    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-row class="justify-content-md-center">
        <b-col md="4">

          <b-form-group id="input-group-username" label="ユーザー名" label-for="input-username">
            <b-form-input id="input-username" v-model="form.username" placeholder="ユーザー名" required></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-email" label="メールアドレス" label-for="input-email">
            <b-form-input id="input-email" v-model="form.email" type="email" placeholder="メールアドレス" required></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-title" label="件名" label-for="input-title">
            <b-form-input id="input-title" v-model="form.username" placeholder="件名" required></b-form-input>
          </b-form-group>

          <b-form-group id="input-textarea-body" label="本文" label-for="textarea-body">
            <b-form-textarea id="textarea-body" v-model="form.body" placeholder="本文" rows="5" max-rows="10"></b-form-textarea>
          </b-form-group>

          <b-form-group id="input-group-agree" v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group v-model="form.checked" id="checkboxes-agree" :aria-describedby="ariaDescribedby">
              <b-form-checkbox>利用規約・プライバシーポリシーに同意する</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="dark">送信</b-button>
          <b-button type="reset" variant="light">リセット</b-button>

        </b-col>
      </b-form-row>

    </b-form>
      
  </div>
</template>

<script>
export default {
  name: 'ContactForm',
  data() {
    return {
      form: {
        username: '',
        email: '',
        title: '',
        body: '',
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
      this.form.email = ''
      this.form.title = ''
      this.form.body = ''
      this.form.checked = []
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>
