<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
}
.layout-logo {
  width: 100px;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  float: left;
  position: relative;
  top: 15px;
  left: 20px;
}
.layout-nav {
  width: 420px;
  margin: 0 auto;
  margin-right: 20px;
}
.layout-footer-center {
  text-align: center;
}
</style>
<template>
  <div class="layout">
    <Layout>
      <Header style="color:white;font-size:75px">我要日物理</Header>
      <Content :style="{padding: '0 50px'}">
        <br />
        <Input
          v-model="KeyWord"
          search
          @on-search="RunSearch()"
          enter-button="Search"
          placeholder="Enter something..."
          size="large"
          height="40"
        />
        <br />
        <Card>
          <div style="min-height: 600px;">Content</div>
        </Card>
      </Content>
      <Footer class="layout-footer-center">2011-2016 &copy; TalkingData</Footer>
    </Layout>
  </div>
</template>
<script>
// import api from "../api";
export default {
  data() {
    return {
      KeyWord: ""
    };
  },
  created() {
    // api.register({ username: "username" });
  },
  methods: {
    RunSearch() {
      console.log(this.KeyWord);
    }
  }
};
</script>