import { defineConfig } from "@archoleat/prettier-define-config";

export default defineConfig({
  overrides: [
    {
      files: ["*.yaml"],
      options: {
        singleQuote: true,
      },
    },
  ],
});
