import { defineConfig } from '@archoleat/prettier-define-config';

export default defineConfig({
  printWidth: 85,
  proseWrap: 'always',
  overrides: [
    {
      files: ['*.js', '*.yaml'],
      options: {
        singleQuote: true,
      },
    },
  ],
});
