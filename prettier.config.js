import { defineConfig } from '@archoleat/prettier-define-config';

export default defineConfig({
  overrides: [
    {
      files: ['*.js', '*.yaml'],
      options: {
        singleQuote: true,
      },
    },
  ],
});
