package com.internship.tool.controller;

import com.internship.tool.entity.FileDocument;
import com.internship.tool.service.FileService;

import org.springframework.core.io.*;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.nio.file.*;

@RestController
@RequestMapping("/api/files")
public class FileController {

    private final FileService service;

    public FileController(FileService service) {
        this.service = service;
    }

    // ✅ POST /upload
    @PostMapping("/upload")
    public ResponseEntity<FileDocument> upload(@RequestParam("file") MultipartFile file) throws Exception {
        return ResponseEntity.ok(service.uploadFile(file));
    }

    // ✅ GET /files/{id}
    @GetMapping("/{id}")
    public ResponseEntity<Resource> download(@PathVariable Long id) throws Exception {

        FileDocument doc = service.getFile(id);

        Path path = Paths.get(doc.getFilePath());
        Resource resource = new UrlResource(path.toUri());

        return ResponseEntity.ok()
                .header(HttpHeaders.CONTENT_DISPOSITION,
                        "attachment; filename=\"" + doc.getOriginalName() + "\"")
                .body(resource);
    }
}