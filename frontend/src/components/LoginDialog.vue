<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="grey darken-2 white--text"
          dark
          v-bind="attrs"
          v-on="on"
        > 
          로그인
        </v-btn>
      </template>
                  <v-card class="elevation-12">
                     <v-toolbar dark color="grey darken-2 white--text">
                        <v-toolbar-title>Login</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text>
                        <v-form>
                           <v-text-field
                              prepend-icon="mail"
                              name="login"
                              label="Email"
                              v-model="email"
                              :rules="emailRules"
                           ></v-text-field>
                           <v-text-field
                              id="password"
                              prepend-icon="lock"
                              name="password"
                              label="Password"
                              type="password"
                           ></v-text-field>
                        </v-form>
                     </v-card-text>
                     <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" to="/">Login</v-btn>
                     </v-card-actions>
                  </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
   name: 'Login',
   props: {
      source: String,
   },
};
</script>

<style></style>


<script>
  export default {
    data: () => ({
      dialog: false,
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
    }),
  }
</script>