package com.internship.tool.service;

import com.internship.tool.entity.FileDocument;
import com.internship.tool.repository.FileRepository;
import com.internship.tool.exception.ResourceNotFoundException;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.nio.file.*;
import java.util.UUID;

@Service
public class FileService {

    @Value("${file.upload-dir}")
    private String uploadDir;

    private final FileRepository repository;

    public FileService(FileRepository repository) {
        this.repository = repository;
    }

    // ✅ UPLOAD
    public FileDocument uploadFile(MultipartFile file) throws Exception {

        // 🔴 VALIDATE SIZE (<10MB)
        if (file.getSize() > 10 * 1024 * 1024) {
            throw new RuntimeException("File size exceeds 10MB");
        }

        // 🔴 VALIDATE TYPE
        String type = file.getContentType();
        if (type == null || 
           !(type.equals("application/pdf") ||
             type.startsWith("image/"))) {
            throw new RuntimeException("Only PDF or Image files allowed");
        }

        // ✅ CREATE FOLDER
        Path uploadPath = Paths.get(uploadDir);
        if (!Files.exists(uploadPath)) {
            Files.createDirectories(uploadPath);
        }

        // ✅ UUID FILE NAME
        String fileName = UUID.randomUUID() + "_" + file.getOriginalFilename();
        Path filePath = uploadPath.resolve(fileName);

        // ✅ SAVE FILE
        Files.copy(file.getInputStream(), filePath, StandardCopyOption.REPLACE_EXISTING);

        // ✅ SAVE IN DB
        FileDocument doc = new FileDocument();
        doc.setOriginalName(file.getOriginalFilename());
        doc.setFileName(fileName);
        doc.setFileType(type);
        doc.setFilePath(filePath.toString());

        return repository.save(doc);
    }

    // ✅ DOWNLOAD
    public FileDocument getFile(Long id) {
        return repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("File not found"));
    }
}